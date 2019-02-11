---
layout: page
title: Themes
permalink: /themes/
---

{% assign matrix_table=site.data.matrix_table %}

{% assign matrix_table=site.data.matrix_table %}
| Name | Description |
| --- | --- |
{%- for themes in matrix_table %}
    {%- if themes[1].enabled == true %}
    {%- assign theme = themes[0] %}
    | <a href="{{ site.url }}/{{ themes[1].file_loc }}">{{ theme }}</a> | _ |
    {%- endif %}
{%- endfor %}