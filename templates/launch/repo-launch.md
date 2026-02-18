---
template_id: repo-launch
category: launch
channels: [mastodon, discord, bluesky, linkedin, ghost]
variables: [repo.name, repo.organ, repo.description, repo.url, event.date, event.tags]
checklist_items:
  - README deployed and reviewed
  - CI pipeline passing
  - Repository description set on GitHub
---

{{#channel mastodon}}
New repository launched in the organvm system:

{{ repo.name }} — {{ repo.description }}

Part of ORGAN {{ repo.organ }}.

{{ repo.url }}

{{#if event.tags}}
#organvm #opensource #{{ repo.organ }}
{{/if}}
{{/channel}}

{{#channel discord}}
**Repository Launch: {{ repo.name }}**

{{ repo.description }}

**Organ:** {{ repo.organ }}
**URL:** {{ repo.url }}
**Date:** {{ event.date }}

This repository is now live and accepting contributions.
{{/channel}}

{{#channel bluesky}}
New in the organvm system: {{ repo.name }}

{{ repo.description }}

{{ repo.url }}
{{/channel}}

{{#channel linkedin}}
Excited to announce the launch of {{ repo.name }}, a new repository in the organvm creative-institutional system.

{{ repo.description }}

This project is part of ORGAN {{ repo.organ }}, contributing to our growing ecosystem of interconnected tools and frameworks.

{{ repo.url }}

#organvm #opensource #software
{{/channel}}
{{#channel ghost}}
# New Repository: {{ repo.name }}

{{ repo.description }}

**Organ:** {{ repo.organ }}

This repository is now live in the organvm creative-institutional system, ready for exploration and contribution.

[View on GitHub]({{ repo.url }})
{{/channel}}
