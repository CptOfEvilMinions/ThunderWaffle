---
layout: page
title: Defacement
category: techniques
permalink: /techniques/actions_on_objective/defacement
---
# `<Technique name> - <technique ID>`

[Website defacement](https://en.wikipedia.org/wiki/Website_defacement) is an attack on a website that changes the visual appearance of the site or a webpage. These are typically the work of defacers, who break into a web server and replace the hosted website with one of their own. Defacement is generally meant as a kind of electronic graffiti and, as other forms of vandalism, is also used to spread messages by politically motivated "cyber protesters" or hacktivists[1].

## Malware/Threat actors

<!-- Threat actors table -->
{% assign threat_actors = site.data.threat_actors %}
{% assign malwares = 'Operation Cleaver' | split: ',' %}

| Name | Type | Description | Year(s) | Source |
| --- | --- | --- | --- | - |
{%- for malware in malwares %}
    {% assign tmp = threat_actors[0][malware] -%}
    | {{ malware }} | {{ tmp.type }} | {{ tmp.description }} | {{ tmp.years }} |
    {%- for source in tmp.sources -%}
        {%- assign source1 = source | split:'/' -%}
            <a href="{{ source }}">{{ source1[-1] }}</a><br>
    {%- endfor -%}
    |
{%- endfor %}

## Mitigations

`<Mitigation techniques>`

## Detections

* A continous service that monitors your website for changes.
* A large number of HTTP requests to a new resource
* A change in packet size when requesting a resource
* Webserver making external requests for resources

## Toolkit

`<Toolkit instructions, if applicable>`

## Resources/Sources

* [Website defacement](https://en.wikipedia.org/wiki/Website_defacement)
