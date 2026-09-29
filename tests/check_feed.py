#!/usr/bin/env python3
"""QA-Gate fuer den RSS-Feed. Aufruf nach dem Hugo-Build: python3 tests/check_feed.py [public]

Bricht mit Exit-Code 1 ab, wenn der Feed kaputt ist — dann wird nicht deployt.
Nur Standardbibliothek, laeuft ohne Installation auf dem GitHub-Runner.
"""
import re
import sys
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

public = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}
errors = []


def check(ok, msg):
    if not ok:
        errors.append(msg)


feed_path = public / "index.xml"
check(feed_path.exists(), f"{feed_path} fehlt")
if errors:
    sys.exit("\n".join(errors))

raw = feed_path.read_text(encoding="utf-8")
try:
    root = ET.fromstring(raw)  # schlaegt bei nicht wohlgeformtem XML fehl
except ET.ParseError as e:
    sys.exit(f"Feed ist kein wohlgeformtes XML: {e}")

check(root.tag == "rss" and root.get("version") == "2.0", "Wurzel ist kein <rss version=\"2.0\">")
channel = root.find("channel")
check(channel is not None, "<channel> fehlt")
if channel is None:
    sys.exit("\n".join(errors))

# --- Channel ---
for tag in ("title", "link", "description", "language", "lastBuildDate", "managingEditor"):
    check((channel.findtext(tag) or "").strip(), f"channel: <{tag}> fehlt oder ist leer")

base = urlparse(channel.findtext("link") or "")
check(base.scheme == "https" or base.hostname in ("localhost", "127.0.0.1"), "channel: <link> ist nicht https")

self_link = channel.find("atom:link[@rel='self']", NS)
check(self_link is not None, "channel: atom:link rel=self fehlt (Autodiscovery/Validator)")
if self_link is not None:
    check(self_link.get("type") == "application/rss+xml", "atom:link self hat falschen type")
    check(self_link.get("href", "").endswith("/index.xml"), "atom:link self zeigt nicht auf /index.xml")

# --- Items ---
items = channel.findall("item")
check(items, "Feed enthaelt keine Beitraege")

# Soll-Anzahl: jeder gebaute Blogbeitrag. Redirect-Stubs aus "aliases:"
# (meta refresh) sind keine Beitraege.
posts = sorted(
    p.parent.name
    for p in (public / "blog").glob("*/index.html")
    if 'http-equiv=refresh' not in p.read_text(encoding="utf-8").replace('"', "")
)
check(len(items) == len(posts) or len(items) == 20,
      f"{len(items)} Feed-Eintraege, aber {len(posts)} gebaute Beitraege")

seen, dates = set(), []
for i, item in enumerate(items, 1):
    where = f"item {i} ({(item.findtext('title') or '?')[:40]})"
    for tag in ("title", "link", "guid", "pubDate", "description"):
        check((item.findtext(tag) or "").strip(), f"{where}: <{tag}> fehlt oder ist leer")

    link = (item.findtext("link") or "").strip()
    guid = item.find("guid")
    check(guid is not None and guid.text == link, f"{where}: guid weicht vom link ab")
    check(link not in seen, f"{where}: doppelter Eintrag {link}")
    seen.add(link)

    path = urlparse(link).path
    check(path.startswith("/blog/") and path != "/blog/", f"{where}: kein Blogbeitrag ({path})")
    check((public / path.lstrip("/") / "index.html").exists(), f"{where}: Ziel {path} existiert nicht im Build")

    try:
        d = parsedate_to_datetime(item.findtext("pubDate"))
        check(d.tzinfo is not None, f"{where}: pubDate ohne Zeitzone")
        dates.append(d)
    except (TypeError, ValueError):
        errors.append(f"{where}: pubDate ist kein RFC-822-Datum")

    check((item.findtext("dc:creator", namespaces=NS) or "").strip(), f"{where}: dc:creator fehlt")
    check(item.findall("category"), f"{where}: keine <category>")

    body = item.findtext("content:encoded", namespaces=NS) or ""
    check(len(body) > 500, f"{where}: content:encoded fehlt oder ist verdaechtig kurz")
    rel = re.findall(r'(?:href|src)="(?!https?:|mailto:|tel:)([^"]*)"', body)
    check(not rel, f"{where}: relative URLs im Inhalt {rel[:3]}")
    check("<script" not in body.lower(), f"{where}: <script> im Feed-Inhalt")

check(dates == sorted(dates, reverse=True), "Eintraege sind nicht nach Datum absteigend sortiert")
now_ok = all(d.timestamp() <= __import__("time").time() + 86400 for d in dates)
check(now_ok, "Feed enthaelt Beitraege mit Datum in der Zukunft")

# Nichts, was nicht in den Feed gehoert
for forbidden in ("/imprint/", "/privacy-policy/", "/about/"):
    check(f"<link>{base.scheme}://{base.netloc}{forbidden}</link>" not in raw,
          f"Seite {forbidden} steht im Feed")

# Stylesheet muss ausgeliefert werden, wenn es referenziert wird
m = re.search(r'<\?xml-stylesheet[^>]*href="([^"]+)"', raw)
if m:
    check((public / m.group(1).lstrip("/")).exists(), f"Stylesheet {m.group(1)} fehlt im Build")

if errors:
    print(f"FEED-CHECK FEHLGESCHLAGEN ({len(errors)}):")
    print("\n".join(f"  - {e}" for e in errors))
    sys.exit(1)
print(f"Feed OK: {len(items)} Eintraege, neuester: {items[0].findtext('title')}")
