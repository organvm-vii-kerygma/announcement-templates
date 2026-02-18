---
template_id: reading-group
category: community
channels: [mastodon, discord, bluesky]
variables: [event.title, event.summary, event.url, event.date, event.book_title, event.author]
checklist_items:
  - Reading material selected
  - Discussion questions prepared
---

{{#channel mastodon}}
Join our reading group:

{{ event.title }}

We'll be discussing "{{ event.book_title }}" by {{ event.author }}.

{{ event.summary }}

{{ event.url }}

#organvm #reading #community
{{/channel}}

{{#channel discord}}
**Reading Group: {{ event.title }}**

**Text:** "{{ event.book_title }}" by {{ event.author }}

{{ event.summary }}

**Date:** {{ event.date }}
**Details:** {{ event.url }}
{{/channel}}

{{#channel bluesky}}
Reading group: {{ event.title }}

"{{ event.book_title }}" by {{ event.author }}

{{ event.url }}
{{/channel}}
