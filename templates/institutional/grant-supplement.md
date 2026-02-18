---
template_id: grant-supplement
category: institutional
channels: [mastodon, discord, linkedin, bluesky, ghost]
variables: [event.title, event.summary, event.url, event.funder, event.date]
checklist_items:
  - Grant funder acknowledged
  - Public disclosure terms verified
---

{{#channel mastodon}}
{{ event.title }}

{{ event.summary }}

{{#if event.funder}}
Supported by {{ event.funder }}.
{{/if}}

{{ event.url }}

#organvm #grant #funding
{{/channel}}

{{#channel discord}}
**Grant Update: {{ event.title }}**

{{ event.summary }}

{{#if event.funder}}
**Funder:** {{ event.funder }}
{{/if}}
**Date:** {{ event.date }}
**Details:** {{ event.url }}
{{/channel}}

{{#channel bluesky}}
{{ event.title }}

{{ event.summary }}

{{ event.url }}
{{/channel}}

{{#channel linkedin}}
{{ event.title }}

{{ event.summary }}

{{#if event.funder}}
We gratefully acknowledge the support of {{ event.funder }} in making this work possible.
{{/if}}

The organvm system continues to grow through institutional support and open collaboration.

{{ event.url }}

#organvm #grant #funding #research
{{/channel}}
{{#channel ghost}}
# {{ event.title }}

{{ event.summary }}

{{#if event.funder}}
We gratefully acknowledge the support of {{ event.funder }} in making this work possible.
{{/if}}

[Details]({{ event.url }})
{{/channel}}
