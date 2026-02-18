---
template_id: essay-highlight
category: essay
channels: [mastodon, discord, bluesky]
variables: [event.title, event.summary, event.url, event.quote]
checklist_items:
  - Key quote selected
  - Original essay URL verified
---

{{#channel mastodon}}
From "{{ event.title }}":

"{{ event.quote }}"

Read the full essay:
{{ event.url }}

#organvm #writing
{{/channel}}

{{#channel discord}}
**Essay Highlight: {{ event.title }}**

> {{ event.quote }}

**Full essay:** {{ event.url }}
{{/channel}}

{{#channel bluesky}}
"{{ event.quote }}"

— from "{{ event.title }}"

{{ event.url }}
{{/channel}}
