---
template_id: partnership
category: institutional
channels: [mastodon, discord, linkedin, bluesky, ghost]
variables: [event.title, event.summary, event.url, event.partner_name, event.date]
checklist_items:
  - Partner approval received
  - Partnership terms documented
---

{{#channel mastodon}}
{{ event.title }}

{{ event.summary }}

In collaboration with {{ event.partner_name }}.

{{ event.url }}

#organvm #partnership
{{/channel}}

{{#channel discord}}
**Partnership Announcement: {{ event.title }}**

{{ event.summary }}

**Partner:** {{ event.partner_name }}
**Date:** {{ event.date }}
**Details:** {{ event.url }}
{{/channel}}

{{#channel bluesky}}
{{ event.title }}

With {{ event.partner_name }}.

{{ event.url }}
{{/channel}}

{{#channel linkedin}}
{{ event.title }}

{{ event.summary }}

We are thrilled to collaborate with {{ event.partner_name }} to advance the organvm creative-institutional ecosystem.

{{ event.url }}

#organvm #partnership #collaboration
{{/channel}}
{{#channel ghost}}
# {{ event.title }}

{{ event.summary }}

In collaboration with {{ event.partner_name }}, this partnership advances the organvm creative-institutional ecosystem.

[Learn more]({{ event.url }})
{{/channel}}
