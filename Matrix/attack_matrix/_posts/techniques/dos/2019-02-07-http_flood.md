---
layout: post
enabled: true
title: HTTP Flood
category: techniques
permalink: /techniques/dos/http_flood
---
# `HTTP flood- <technique ID>`

An [HTTP flood attack](https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack/) is a type of volumetric distributed denial-of-service (DDoS) attack designed to overwhelm a targeted server with HTTP requests. Once the target has been saturated with requests and is unable to respond to normal traffic, denial-of-service will occur for additional requests from actual users.

## Malware/Threat actors

{% assign malwares = 'DarkComet' | split: ',' %}

{% capture my_include %}{% include threat_actor_table.md %}{% endcapture %}{{ my_include | markdownify }}

## Mitigations

Mitigating layer 7 attacks is complex and often multifaceted. One method is to implement a challenge to the requesting machine in order to test whether or not it is a bot, much like a captcha test commonly found when creating an account online. By giving a requirement such as a JavaScript computational challenge, many attacks can be mitigated.

## Detections

Avenues for stopping HTTP floods include the use of a web application firewall (WAF), managing an IP reputation database in order to track and selectively block malicious traffic.

## Toolkit

`<Toolkit instructions, if applicable>`

## Resources/Sources

* [What is an HTTP flood DDoS attack?](https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack/)
