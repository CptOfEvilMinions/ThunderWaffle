---
layout: page
title: Threat actors
permalink: /threat_actors/
---

{% assign threat_actors = site.data.threat_actors %}
| Name | Type | Description | Year(s) | Source |
| --- | --- | --- | --- | - |
{%- for threat_actor in threat_actors[0] %}
    {% assign tmp = threat_actor[1] -%}
    | {{ threat_actor[0] }} | {{ tmp.type }} | {{ tmp.description }} | {{ tmp.years }} |
    {%- for source in tmp.sources -%}
        {%- assign source1 = source | split:'/' -%}
            <a href="{{ source }}">{{ source1[-1] }}</a><br>
    {%- endfor -%}
    |
{%- endfor %}