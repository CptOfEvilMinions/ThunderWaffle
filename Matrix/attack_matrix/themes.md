---
layout: page
title: Themes
permalink: /themes/
---

| Name | Description |
| --- | --- |
{%- for post in site.categories.themes %}
    {%- if post.enabled == true %}
        | <a href="{{ site.url }}/{{ post.permalink }}">{{ post.title }}</a> | {{ post.description }} |
    {%- endif -%}
{%- endfor %}