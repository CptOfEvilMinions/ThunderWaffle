---
layout: post
enabled: true
title: "Listening Service"
category: techniques
theme: command_and_control
Id: 04
description: ""
---
{{ page. description }}



## Malware/Threat actors

{% assign malwares = 'Gh0st Rat' | split: ',' %}

{% capture my_include %}{% include threat_actor_table.md %}{% endcapture %}{{ my_include | markdownify }}

## Mitigations

`<Mitigation techniques>`

## Detections

`<Detection techniques>`

## Toolkit

`<Toolkit instructions, if applicable>`

## Resources/Sources

* `[<Source name>](<Source link>)`
