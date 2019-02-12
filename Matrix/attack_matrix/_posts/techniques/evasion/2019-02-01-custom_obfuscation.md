---
layout: post
enabled: true
title: 'Custom obfuscation'
category: techniques
theme: Evasion
Id: 14
description: 'Threat actors may create custom obfuscation(encryption, encoding, and hashing) mechaniss to thwart defenders.'
permalink: /techniques/evasion/custom_obfuscation
---
{{ page. description }}



## Common types

* encryption
* obfuscation
* compression

## Malware/Threat actors

{% assign malwares = 'TeamSpy,Wild Neutron' | split: ',' %}

{% include threat_actor_table.html %}

## Mitigations

`<Mitigation techniques>`

## Detections

During the encryption handshake in protocols like TLS, SSL, and SSH look for encryption suites and ciphers that are new to the enviornment.

## Toolkit

`<Toolkit instructions, if applicable>`

## Resources/Sources

* [Github - CyberMonitor/APT_CyberCriminal_Campagin_Collections](https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections)