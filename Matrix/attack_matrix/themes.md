---
layout: page
title: Themes
permalink: /themes/
---

| Name | Description |
| --- | --- |
{%- for post in site.posts %}
    {%- if post.category == "themes" and post.title != "Template" %}
        | <a href="{{ site.url }}/{{ post.permalink }}">{{ post.title }}</a> | {{ post.description }} |
    {%- endif %}
{%- endfor -%}