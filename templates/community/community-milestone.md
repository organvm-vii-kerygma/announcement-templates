---
template_id: community-milestone
category: community
channels: [mastodon, discord, bluesky, ghost]
variables: [milestone.title, milestone.type, milestone.summary, milestone.source_organ, milestone.issue_url]
checklist_items:
  - Community approval verified (7-day RFC)
  - Quality threshold met
---

{{#channel mastodon}}
Community milestone reached:

{{ milestone.title }}

{{ milestone.summary }}

Approved through our community RFC process.

{{ milestone.issue_url }}

#organvm #community #milestone
{{/channel}}

{{#channel discord}}
**Community Milestone: {{ milestone.title }}**

{{ milestone.summary }}

**Type:** {{ milestone.type }}
**Source:** {{ milestone.source_organ }}
**Details:** {{ milestone.issue_url }}

This milestone passed our 7-day community review process.
{{/channel}}

{{#channel bluesky}}
Community milestone: {{ milestone.title }}

{{ milestone.summary }}

{{ milestone.issue_url }}
{{/channel}}
{{#channel ghost}}
# Community Milestone: {{ milestone.title }}

{{ milestone.summary }}

**Milestone type:** {{ milestone.type }}
**Originating organ:** {{ milestone.source_organ }}

This initiative was approved through our community RFC process, which requires a minimum 7-day review period and quality threshold verification before announcement.

[View the full discussion]({{ milestone.issue_url }})
{{/channel}}
