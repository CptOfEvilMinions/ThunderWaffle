---
layout: page
title: ARP spoofing
category: techniques
permalink: /techniques/masquerade/arp_spoofing
---
# `ARP spoofing- <technique ID>`

[ARP spoofing](https://www.veracode.com/security/arp-spoofing) is a type of attack in which a malicious actor sends falsified ARP (Address Resolution Protocol) messages over a local area network. This results in the linking of an attacker’s MAC address with the IP address of a legitimate computer or server on the network. Once the attacker’s MAC address is connected to an authentic IP address, the attacker will begin receiving any data that is intended for that IP address. ARP spoofing can enable malicious parties to intercept, modify or even stop data in-transit. ARP spoofing attacks can only occur on local area networks that utilize the Address Resolution Protocol.

## Malware/Threat actors

| Name | Description | Year(s) | Source |
| --- | --- | --- |
| `SIDEWINDER` | - | - | - |
| `Operation Cleaver` | --- | --- | --- |

## Mitigations

* Packet filtering: Packet filters inspect packets as they are transmitted across a network. Packet filters are useful in ARP spoofing prevention because they are capable of filtering out and blocking packets with conflicting source address information (packets from outside the network that show source addresses from inside the network and vice-versa).

## Detections

* Use ARP spoofing detection software: There are many programs available that help organizations detect ARP spoofing attacks. These programs work by inspecting and certifying data before it is transmitted and blocking data that appears to be spoofed.

## Toolkit

`<Toolkit instructions, if applicable>`

## Resources/Sources

* [ARP SPOOFING](https://www.veracode.com/security/arp-spoofing)
