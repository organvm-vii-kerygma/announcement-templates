---
template_id: contribution-merged
category: community
channels: [mastodon, discord, bluesky, linkedin, ghost]
variables: [contrib.project_name, contrib.project_org, contrib.pr_number, contrib.pr_title, contrib.pr_url, contrib.problem, contrib.solution, contrib.language, contrib.project_significance]
checklist_items:
  - PR merged and verified on upstream
  - Backflow manifest updated with merged state
  - LinkedIn draft reviewed for tone and accuracy
---

{{#channel mastodon}}
Contribution merged into {{ contrib.project_org }}/{{ contrib.project_name }}:

{{ contrib.pr_title }}

{{ contrib.problem }}

{{ contrib.pr_url }}

#opensource #{{ contrib.language }}
{{/channel}}

{{#channel discord}}
**Contribution Merged: {{ contrib.project_org }}/{{ contrib.project_name }}**

**PR:** #{{ contrib.pr_number }} — {{ contrib.pr_title }}

**Problem:** {{ contrib.problem }}

**Solution:** {{ contrib.solution }}

**Language:** {{ contrib.language }}
**Link:** {{ contrib.pr_url }}
{{/channel}}

{{#channel bluesky}}
Merged into {{ contrib.project_org }}/{{ contrib.project_name }}: {{ contrib.pr_title }}

{{ contrib.pr_url }}
{{/channel}}

{{#channel linkedin}}
Contributed a fix to {{ contrib.project_name }} ({{ contrib.project_org }}) — {{ contrib.project_significance }}

{{ contrib.problem }}

{{ contrib.solution }}

{{ contrib.pr_url }}

#OpenSource #{{ contrib.language }} #SoftwareEngineering #DevTools
{{/channel}}

{{#channel ghost}}
# Contribution Merged: {{ contrib.project_name }}

**Repository:** {{ contrib.project_org }}/{{ contrib.project_name }}
**PR:** [#{{ contrib.pr_number }} — {{ contrib.pr_title }}]({{ contrib.pr_url }})
**Language:** {{ contrib.language }}

## Problem

{{ contrib.problem }}

## Solution

{{ contrib.solution }}

## Why This Matters

{{ contrib.project_significance }}
{{/channel}}
