---
layout: page
title: Techniques
permalink: /technqiues
---

| Name | Id | Theme | Description |
| --- | --- | --- | --- |
{%- for post in site.categories.techniques %}
    {%- if post.enabled == true %}
        | <a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a> | {{ post.Id }} | {{ post.theme }} | {{ post.description }} |
    {%- endif -%}
{%- endfor -%}

