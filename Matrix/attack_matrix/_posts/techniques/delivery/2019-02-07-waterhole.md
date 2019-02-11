---
layout: post
enabled: true
title: Waterhole
category: techniques
permalink: /techniques/delivery/waterhole
---
# `Waterhole - <technique ID>`

A [watering hole attack](https://searchsecurity.techtarget.com/definition/watering-hole-attack) is a security exploit in which the attacker seeks to compromise a specific group of end users by infecting websites that members of the group are known to visit. The goal is to infect a targeted user's computer and gain access to the network at the target's place of employment.

## Types

* Java exploits
* Flash exploits
* Internet Explorer(IE)
* JAR
* HTML

## Malware/Threat actors

{% assign malwares = 'Operation Dust Storm,ZooPark,Operation Cleaver,Epic Turla,Energetic Bear' | split: ',' %}

{% include threat_actor_table.md %}

## Mitigations

* Keep all commonly used software and operating systems patched and updated to the latest versions
* Inspect all popular websites that employees visit and routinely inspect these sites for malware
* Configure browsers or other tools to use website reputation services to notify users of known, bad websites

## Detections

* Collect user-agents and alert on oold versions of flash and IE

## Toolkit

`<Toolkit instructions, if applicable>`

## Resources/Sources

* [Watering hole attack](https://searchsecurity.techtarget.com/definition/watering-hole-attack)
* [Network Security and Watering Hole Attacks](https://www.lastline.com/blog/network-security-and-watering-hole-attacks/)
