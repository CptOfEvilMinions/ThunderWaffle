# Setup Bro/Zeek

### Setup Bro with splunk forwarder

#### Setup Splunk

1. Open browser to `https://www.splunk.com/en_us/download` and login
1. Download latest splunk forwarder
1. Place splunkforwarder-*-amd64.deb inti files/splunk named as splunkforwarder.deb

## Setup Bro

1. `mv group_vars/bro.example group_vars/bro.yml`
1. `vim group_vars/splunk.yml` and set:
    1. `bro_management_interface` - Interface to access Bro box via SSH
    1. `bro_promiscuous_interface` - Interface to monitor network traffic
    1. `bro_local_network` - Local network that BRO is monitoring
        2. Example: `192.168.1.0/24`
    1. `bro_mail_to` - Location to send e-mails
1. `vim hosts.yml` and under "[bro]" set:
    1. `ansible_host` - Set to IP addr of remote host
1. `ansible-playbook -i hosts.yml deploy_bro.yml -u <username> -K`
    1. Be patient the make process may take 20+ mins

## Resources/Sources

### Bro/Zeek

* [Confiure Bro for Splunk](https://undercoverelephant.info/2018/02/07/configuring-bro-for-splunk/)