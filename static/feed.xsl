<?xml version="1.0" encoding="utf-8"?>
<!-- Macht den Feed im Browser lesbar. Feedreader ignorieren dieses
     Stylesheet und lesen das XML direkt. -->
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:dc="http://purl.org/dc/elements/1.1/">
  <xsl:output method="html" encoding="utf-8" indent="yes"/>
  <xsl:template match="/rss/channel">
    <html lang="en">
      <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width,initial-scale=1"/>
        <meta name="robots" content="noindex"/>
        <title><xsl:value-of select="title"/> (RSS feed)</title>
        <style>
          body { margin: 0; background: #E6D8C9; color: #2b2b2b; font: 1.0625rem/1.6 system-ui, sans-serif; }
          main { max-width: 820px; margin: 0 auto; padding: 2rem 1rem 4rem; }
          .notice { background: #F7F7F5; border-left: 4px solid #5F7360; padding: 1rem 1.25rem; margin-bottom: 2rem; }
          a { color: #4A5C4B; }
          h1 { margin-top: 0; }
          article { padding: 1.25rem 0; border-top: 1px solid rgba(0,0,0,.15); }
          article h2 { margin: 0 0 .25rem; font-size: 1.25rem; }
          .meta { color: #4A4A4A; font-size: .9rem; margin: 0 0 .5rem; }
          @media (prefers-color-scheme: dark) {
            body { background: #1c1f1c; color: #ece9e2; }
            .notice { background: #262a26; border-color: #9db19e; }
            a { color: #b7cbb8; }
            .meta { color: #c4c1b9; }
            article { border-color: rgba(255,255,255,.18); }
          }
        </style>
      </head>
      <body>
        <main>
          <div class="notice">
            <strong>This is an RSS feed.</strong>
            Copy this page's address into a feed reader to follow new posts.
            <a href="{link}"><xsl:attribute name="href"><xsl:value-of select="link"/></xsl:attribute>Visit the website →</a>
          </div>
          <h1><xsl:value-of select="title"/></h1>
          <p><xsl:value-of select="description"/></p>
          <xsl:for-each select="item">
            <article>
              <h2><a><xsl:attribute name="href"><xsl:value-of select="link"/></xsl:attribute><xsl:value-of select="title"/></a></h2>
              <p class="meta"><xsl:value-of select="substring(pubDate, 6, 11)"/> · <xsl:value-of select="dc:creator"/></p>
              <p><xsl:value-of select="description"/></p>
            </article>
          </xsl:for-each>
        </main>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
