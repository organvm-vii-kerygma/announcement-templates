---
template_id: bugfix-release
category: release
channels: [mastodon, discord, bluesky, ghost]
variables: [repo.name, repo.url, event.summary, event.version, event.date]
checklist_items:
  - Bug root cause documented
  - Regression test added
  - CHANGELOG updated
---

{{#channel mastodon}}
{{ repo.name }} {{ event.version }} — bugfix release

{{ event.summary }}

{{ repo.url }}

#organvm #bugfix
{{/channel}}

{{#channel discord}}
**Bugfix: {{ repo.name }} {{ event.version }}**

{{ event.summary }}

**Repo:** {{ repo.url }}
**Date:** {{ event.date }}
{{/channel}}

{{#channel bluesky}}
Bugfix: {{ repo.name }} {{ event.version }}

{{ event.summary }}

{{ repo.url }}
{{/channel}}
{{#channel ghost}}
# Bugfix: {{ repo.name }} {{ event.version }}

{{ event.summary }}

[View release]({{ repo.url }})
{{/channel}}
