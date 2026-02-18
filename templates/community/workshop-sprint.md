---
template_id: workshop-sprint
category: community
channels: [mastodon, discord, bluesky]
variables: [event.title, event.summary, event.url, event.date, event.duration]
checklist_items:
  - Workshop materials prepared
  - Participant instructions documented
---

{{#channel mastodon}}
Workshop sprint: {{ event.title }}

{{ event.summary }}

{{ event.date }} ({{ event.duration }})

{{ event.url }}

#organvm #workshop #sprint
{{/channel}}

{{#channel discord}}
**Workshop Sprint: {{ event.title }}**

{{ event.summary }}

**When:** {{ event.date }}
**Duration:** {{ event.duration }}
**Details:** {{ event.url }}
{{/channel}}

{{#channel bluesky}}
Workshop: {{ event.title }}

{{ event.summary }}

{{ event.date }} — {{ event.url }}
{{/channel}}
