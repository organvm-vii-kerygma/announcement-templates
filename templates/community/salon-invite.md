---
template_id: salon-invite
category: community
channels: [mastodon, discord, bluesky]
variables: [event.title, event.summary, event.url, event.date, event.time, event.location]
checklist_items:
  - Event date and time confirmed
  - RSVP mechanism set up
---

{{#channel mastodon}}
You're invited to an organvm salon:

{{ event.title }}

{{ event.summary }}

{{ event.date }} at {{ event.time }}

{{ event.url }}

#organvm #salon #community
{{/channel}}

{{#channel discord}}
**Salon Invitation: {{ event.title }}**

{{ event.summary }}

**When:** {{ event.date }} at {{ event.time }}
**Where:** {{ event.location }}
**Details:** {{ event.url }}
{{/channel}}

{{#channel bluesky}}
Salon: {{ event.title }}

{{ event.summary }}

{{ event.date }} — {{ event.url }}
{{/channel}}
