---
layout: post
enabled: true
title: Custom obfuscation
category: techniques
permalink: /techniques/evasion/custom_obfuscation
---
# `Custom encryption - <technique ID>`

Threat actors may create custom obfuscation(encryption, encoding) to thwart defenders.

## Common types

* encryption
* obfuscation
* compression

## Malware/Threat actors

{% assign malwares = 'TeamSpy,Wild Neutron' | split: ',' %}

{% include_relative threat_actor_table.md %}

## Mitigations

`<Mitigation techniques>`

## Detections

During the encryption handshake in protocols like TLS, SSL, and SSH look for encryption suites and ciphers that are new to the enviornment.

## Toolkit

`<Toolkit instructions, if applicable>`

## Resources/Sources

* [Github - CyberMonitor/APT_CyberCriminal_Campagin_Collections](https://github.com/CyberMonitor/APT_CyberCriminal_Campagin_Collections)