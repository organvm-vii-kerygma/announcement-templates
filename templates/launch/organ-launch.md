---
template_id: organ-launch
category: launch
channels: [mastodon, discord, bluesky, linkedin, ghost]
variables: [event.title, event.summary, event.url, event.organ, event.date]
checklist_items:
  - All organ repos documented
  - Profile README deployed
  - Registry updated to OPERATIONAL
---

{{#channel mastodon}}
{{ event.title }}

{{ event.summary }}

{{ event.url }}

#organvm #{{ event.organ }} #launch
{{/channel}}

{{#channel discord}}
**{{ event.title }}**

{{ event.summary }}

**Organ:** {{ event.organ }}
**Date:** {{ event.date }}
**URL:** {{ event.url }}
{{/channel}}

{{#channel bluesky}}
{{ event.title }}

{{ event.summary }}

{{ event.url }}
{{/channel}}

{{#channel linkedin}}
{{ event.title }}

{{ event.summary }}

This marks a significant milestone in the organvm creative-institutional system — a new organ is now fully operational.

{{ event.url }}

#organvm #launch #opensource
{{/channel}}
{{#channel ghost}}
# {{ event.title }}

{{ event.summary }}

This marks a significant milestone in the organvm creative-institutional system — a new organ is now fully operational and contributing to the eight-organ architecture.

[Learn more]({{ event.url }})
{{/channel}}
