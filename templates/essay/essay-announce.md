---
template_id: essay-announce
category: essay
channels: [mastodon, discord, bluesky, linkedin]
variables: [event.title, event.summary, event.url, event.date, event.tags]
checklist_items:
  - Essay published to GitHub Pages
  - RSS feed updated
  - Canonical URL verified
---

{{#channel mastodon}}
New essay published:

"{{ event.title }}"

{{ event.summary }}

{{ event.url }}

#organvm #writing #essay
{{/channel}}

{{#channel discord}}
**New Essay: {{ event.title }}**

{{ event.summary }}

**Read:** {{ event.url }}
**Published:** {{ event.date }}
{{/channel}}

{{#channel bluesky}}
New essay: "{{ event.title }}"

{{ event.summary }}

{{ event.url }}
{{/channel}}

{{#channel linkedin}}
New essay published in the organvm public process:

"{{ event.title }}"

{{ event.summary }}

{{ event.url }}

#organvm #writing #essay
{{/channel}}
