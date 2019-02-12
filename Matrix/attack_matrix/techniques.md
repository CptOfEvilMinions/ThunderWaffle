---
layout: page
title: Techniques
permalink: /technqiues
---

| Name | Id | Theme | Description |
| --- | --- | --- | --- |
{%- for post in site.categories.techniques %}
    {%- if post.enabled == true %}
        | <a href="{{ site.url }}{{ post.permalink }}">{{ post.title }}</a> | {{ post.Id }} | {{ post.theme }} | {{ post.description }} |
    {%- endif -%}
{%- endfor -%}

