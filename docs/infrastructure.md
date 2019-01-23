# Infrastructure

## Init setup

1. `mv group_vars/all.example group_vars/all.yml`
1. `vim group_vars/all.yml` and set:
    1. `hostname` - Set hostname for box
    1. `base_domain` - Set the domain for the box
    1. `Cert generation`- Insert values
    1. `slack_channel` - OPTIONAL - Set to Slack channel
    1. `slack_token` - OPTIONAL - Set to Slack channel token

## Setup infrastructure

1. [Setup Docker](docs/infra/docker.md)
1. [Setup Rsyslog](docs/infra/rsyslog.md)
1. [Setup Splunk](docs/infra/splunk.md)
1. [Setup Bro/Zeek](docs/infra/zeek.md)

## Supported OSes

* Ubuntu Server 18.04 64-bit