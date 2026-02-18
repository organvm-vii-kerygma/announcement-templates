---
template_id: essay-series
category: essay
channels: [mastodon, discord, bluesky, linkedin]
variables: [event.title, event.summary, event.url, event.series_name, event.part_number, event.date]
checklist_items:
  - Previous parts linked in essay
  - Series index page updated
---

{{#channel mastodon}}
New in the "{{ event.series_name }}" series (Part {{ event.part_number }}):

"{{ event.title }}"

{{ event.summary }}

{{ event.url }}

#organvm #writing #series
{{/channel}}

{{#channel discord}}
**Essay Series: {{ event.series_name }} — Part {{ event.part_number }}**

"{{ event.title }}"

{{ event.summary }}

**Read:** {{ event.url }}
**Published:** {{ event.date }}
{{/channel}}

{{#channel bluesky}}
"{{ event.series_name }}" Part {{ event.part_number }}: {{ event.title }}

{{ event.summary }}

{{ event.url }}
{{/channel}}

{{#channel linkedin}}
Part {{ event.part_number }} of the "{{ event.series_name }}" essay series is now live:

"{{ event.title }}"

{{ event.summary }}

{{ event.url }}

#organvm #writing #series
{{/channel}}
