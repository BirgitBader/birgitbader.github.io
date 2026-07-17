---
title: "Finally talking about API docs"
date: 2026-05-30
draft: false
---

Friends, how much longer were you supposed to wait until I finally post something about API docs?! Waiting is over. Here we go. I’ve actually procrastinated on this topic for quite a while, because I had too much to say, that I genuinely didn’t know where to begin. So let’s start with the basics first.

### APIs are everywhere

We interact with APIs constantly, even if we’re not developers ourselves. Your weather app? API. Paying with PayPal? API. Spotify, Google Maps, “Login with Google” ? APIs everywhere.  
At the core, an API is just a way for systems to communicate with each other. One application sends a request, another responds with data. A simple idea with a huge impact.  
  
What makes APIs so powerful is abstraction. You don’t need to understand an entire backend system to use it. You just need to know things like:  
  
- What can I request?  
- What does the request need to look like?  
- What do I get back?  
  
That’s the contract and where API docs become vital.

### API docs are where products become usable

I fell in love with APIs and API docs back in 2015. Since then, I think API documentation is one of the most underrated parts of software development. Yet they are precisely the level at which complexity finally becomes understandable.  Where systems stop feeling abstract and start feeling usable. A good API can expose powerful functionality. Good API docs make people actually want to use it.   
  
Because developers rarely experience a product through architecture diagrams or internal engineering decisions. They experience it through onboarding flows, authentication, examples, SDKs, error messages, and documentation. Through the feeling of: “Okay, I get this.”  
That first successful request matters more than many API providers realize. The second somebody gets a working response back, trust starts building.

### The best API docs create clarity

The API docs I remember most are usually not the most technically impressive ones. They’re the ones that made things click quickly through clear structure, good examples, straightforward language, and thoughtful naming. The right information exactly when you need it. That sounds obvious, but it’s surprisingly rare. Luckily, [Stripe](https://docs.stripe.com/api), for example, does an incredibly good job here!   
  
A lot of developers don’t want long explanations first. They want a working request. A copy-paste example. Something they can test immediately. The really good API docs understand that. They anticipate friction before it happens. They explain authentication properly, show realistic requests and responses instead of polished demo data, tell you what happens when things fail and explain rate limits before someone accidentally runs into them at 2am and starts questioning their life choices. That kind of clarity takes work.

### API docs are no longer just for humans 

I observe that the role of API docs is changing a lot right now because of AI. Documentation is no longer provided only for developers reading it manually. Machines consume it too. 

AI coding assistants, agents, MCP servers, internal copilots: they all rely on structured, understandable documentation to interact with APIs correctly.  Which means API docs suddenly have two audiences: humans and machines. And more than ever they do have strategic value!

  
No surprise, the qualities that help humans do help AI too, such as clear naming, consistent structures, explicit error handling, good examples, or predictable schemas.  Bad documentation confuses developers and AI.  With AI "in the room", API documentation is no longer just surrounding the interface. In many ways, it _is_ part of the interface now.

### APIs are communication

That’s probably why I find API docs so fascinating. You constantly balance precision with clarity. Technical depth with accessibility. You’re translating systems into understanding. Unlike many other forms of writing, API docs are deeply practical. People use them while building something. While debugging. Usually while slightly stressed and trying to make something work quickly. Which means: every sentence matters.  
  
A confusing authentication section can block an entire integration. A missing example or undocumented property can waste an hour. One good curl request can suddenly unlock everything. People sometimes talk about APIs as purely technical objects, but they’re also communication tools. Every endpoint design decision or response format communicates something. Every line of documentation says something about how well someone understands the people building with their product.   
  
To me, great API docs have always felt surprisingly human and empathetic. Even now, as AI increasingly consumes them too, their real strength is still the same: they respect the developer’s time, attention, and mental energy.