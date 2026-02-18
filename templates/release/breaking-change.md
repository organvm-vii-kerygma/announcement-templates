---
template_id: breaking-change
category: release
channels: [mastodon, discord, bluesky, ghost]
variables: [repo.name, repo.url, event.title, event.summary, event.version, event.date]
checklist_items:
  - Migration guide written
  - Breaking changes documented in CHANGELOG
  - Downstream dependents notified
---

{{#channel mastodon}}
Breaking change in {{ repo.name }} {{ event.version }}

{{ event.summary }}

Please review the migration guide before upgrading.

{{ repo.url }}

#organvm #breaking #migration
{{/channel}}

{{#channel discord}}
**Breaking Change: {{ repo.name }} {{ event.version }}**

{{ event.summary }}

Please review the migration guide before upgrading. Downstream repos may need updates.

**Repo:** {{ repo.url }}
**Date:** {{ event.date }}
{{/channel}}

{{#channel bluesky}}
Breaking change: {{ repo.name }} {{ event.version }}

{{ event.summary }}

{{ repo.url }}
{{/channel}}
{{#channel ghost}}
# Breaking Change: {{ repo.name }} {{ event.version }}

{{ event.summary }}

Please review the migration guide before upgrading. Downstream repositories may need updates.

[Migration guide]({{ repo.url }})
{{/channel}}
