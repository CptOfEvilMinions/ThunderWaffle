---
layout: post
enabled: true
title: Remote Admin Tools
category: techniques
theme: "Command and control"
Id: 05
description: 'Remote Administration tools like TeamViewer can be used to control a machine remotely. Tools like TeamViewer are legitamite applications that are signed and may be trusted by security controls.'
permalink: /techniques/commmand_and_control/remote_admin_tools
---
{{ page.description }}

## Malware/Threat actors

{% assign malwares = 'TeamSpy' | split: ',' %}

{% include threat_actor_table.html %}

## Tools

* [TeamViewer](https://www.teamviewer.com/en-us/)

## Mitigations

`<Mitigation techniques>`

## Detections

`<Detection techniques>`

## Toolkit

`<Toolkit instructions, if applicable>`

## Resources/Sources

* [Github - CyberMonitor/APT_CyberCriminal_Campagin_Collections](https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections)