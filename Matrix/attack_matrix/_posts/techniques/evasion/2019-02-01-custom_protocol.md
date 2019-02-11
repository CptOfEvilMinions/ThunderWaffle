---
layout: post
enabled: true
title: Custom protocol
category: techniques
permalink: /techniques/evasion/custom_protocol
---
# `Custom encryption - <technique ID>`

Threat actors may create custom protcols to thwart security controls from reading the data in transit.

## Common types

* TCP
* Traffic over port 443 that is not HTTPS

## Malware/Threat actors

{% assign malwares = 'Wild Neutron,icefog,APT1,Duqu Trojan,Turbo' | split: ',' %}

{% include threat_actor_table.md %}

## Mitigations

`<Mitigation techniques>`

## Detections

During the encryption handshake in protocols like TLS, SSL, and SSH look for encryption suites and ciphers that are new to the enviornment.

## Toolkit

`<Toolkit instructions, if applicable>`
