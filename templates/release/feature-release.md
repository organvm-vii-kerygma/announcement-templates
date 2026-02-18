---
template_id: feature-release
category: release
channels: [mastodon, discord, bluesky, ghost]
variables: [repo.name, repo.url, event.title, event.summary, event.version, event.date]
checklist_items:
  - CHANGELOG updated
  - Tests passing
  - Version bumped
---

{{#channel mastodon}}
{{ repo.name }} {{ event.version }} released!

{{ event.summary }}

{{ repo.url }}

#organvm #release
{{/channel}}

{{#channel discord}}
**Release: {{ repo.name }} {{ event.version }}**

{{ event.summary }}

**Repo:** {{ repo.url }}
**Date:** {{ event.date }}
{{/channel}}

{{#channel bluesky}}
{{ repo.name }} {{ event.version }} — {{ event.summary }}

{{ repo.url }}
{{/channel}}
{{#channel ghost}}
# {{ repo.name }} {{ event.version }}

{{ event.summary }}

[View release]({{ repo.url }})
{{/channel}}
