---
layout: page
title: Techniques
permalink: /techniques/
---

{% assign matrix_table=site.data.matrix_table %}
| Name | Id | Theme |
| --- | --- | --- |
{%- for themes in matrix_table %}
    {%- assign theme = themes[0] %}
    {%- assign techniques = themes[1] %}
    {%- for technique in techniques %}
        {%- if technique[0] != "enabled" and technique[0] != "file_loc" and technique[1].enabled == true %}
            | <a href="{{ site.url }}/{{ technique[1].file_loc }}">{{ technique[0]}}</a> | {{ technique[1].Id }} | {{ theme }} |
        {%- endif %}
    {%- endfor %}
{%- endfor %}
