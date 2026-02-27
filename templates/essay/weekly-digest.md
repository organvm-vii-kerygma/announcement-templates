---
template_id: weekly-digest
category: essay
channels: [ghost]
variables: [digest.week_label, digest.essay_1_title, digest.essay_1_url, digest.essay_1_summary, digest.essay_2_title, digest.essay_2_url, digest.essay_2_summary, digest.essay_3_title, digest.essay_3_url, digest.essay_3_summary, digest.site_url]
checklist_items:
  - All three essays published and accessible
  - URLs verified
  - Newsletter slug configured in Ghost
---

{{#channel ghost}}
# Weekly Digest — {{ digest.week_label }}

This week on the Public Process:

---

## {{ digest.essay_1_title }}

{{ digest.essay_1_summary }}

[Read the full essay]({{ digest.essay_1_url }})

---

## {{ digest.essay_2_title }}

{{ digest.essay_2_summary }}

[Read the full essay]({{ digest.essay_2_url }})

---

## {{ digest.essay_3_title }}

{{ digest.essay_3_summary }}

[Read the full essay]({{ digest.essay_3_url }})

---

That's all for this week. New essays publish Monday, Wednesday, and Friday.

[Browse all essays]({{ digest.site_url }})
{{/channel}}
