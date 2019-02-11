---
layout: page
title: Techniques
permalink: /techniques/
---

| Name | Id | Theme | Description |
| --- | --- | --- | --- |
{%- for post in site.posts %}
    {%- if post.category == "techniques" and post.title != "Template" %}
        | <a href="{{ site.url }}/{{ post.permalink }}">{{ post.title }}</a> | {{ post.Id }} | {{ post.theme }} | {{ post.description }} |
    {%- endif %}
{%- endfor -%}

<br><br>
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
