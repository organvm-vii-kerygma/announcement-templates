---
template_id: press-release
category: institutional
channels: [mastodon, discord, linkedin]
variables: [event.title, event.summary, event.url, event.date, event.contact]
checklist_items:
  - Press release reviewed for accuracy
  - Contact information verified
  - Embargo date confirmed
---

{{#channel mastodon}}
{{ event.title }}

{{ event.summary }}

{{ event.url }}

#organvm #press
{{/channel}}

{{#channel discord}}
**Press Release: {{ event.title }}**

{{ event.summary }}

**Date:** {{ event.date }}
**Details:** {{ event.url }}
{{#if event.contact}}
**Contact:** {{ event.contact }}
{{/if}}
{{/channel}}

{{#channel linkedin}}
{{ event.title }}

{{ event.summary }}

The organvm project continues to push the boundaries of creative-institutional systems, building open-source infrastructure for art, governance, and public process.

{{ event.url }}

#organvm #press #announcement
{{/channel}}
