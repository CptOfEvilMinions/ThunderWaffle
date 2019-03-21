# Setup Bro/Zeek

## Setup Bro

1. `vim group_vars/logging.yml` and set:
    1. `bro_management_interface` - Interface to access Bro box via SSH
    1. `bro_promiscuous_interface` - Interface to monitor network traffic
    1. `bro_local_network` - Local network that BRO is monitoring
        2. Example: `192.168.1.0/24`
    1. `bro_mail_to` - Location to send e-mails
1. `vim hosts.yml` and under "[bro]" set:
    1. `ansible_host` - Set to IP addr of remote host
1. `ansible-playbook -i hosts.ini deploy_bro.yml -u <username> -K`
    1. Be patient the make process may take 20+ mins

## Supported OSes
* Ubuntu Server 18.04.1 64-bit

## Resources/Sources

### Bro/Zeek

* [Confiure Bro for Splunk](https://undercoverelephant.info/2018/02/07/configuring-bro-for-splunk/)
* [ReadTheDocs - Zeek - Install](https://docs.zeek.org/en/stable/install/install.html)
* [ReadTheDocs - Zeek - GeoIP](https://docs.zeek.org/en/stable/frameworks/geoip.html)
* [MaxMind GeoIP database download](http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz)
* [Installing Bro IDS on Fedora 25](https://www.vultr.com/docs/installing-bro-ids-on-fedora-25)
* [BroControl](https://www.bro.org/sphinx/components/broctl/README.html)
* [How To Install EPEL Repo on a CentOS and RHEL 7.x](https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/)
* [Writing Bro Plugins](https://www.bro.org/sphinx-git/devel/plugins.html)
* [extract-all-files.bro](https://www.bro.org/sphinx/scripts/policy/frameworks/files/extract-all-files.bro.html)
* [stats.bro](https://www.bro.org/sphinx/scripts/policy/misc/stats.bro.html)
* [Bro Package Manager: list of packages](http://blog.bro.org/2017/06/bro-package-manager-list-of-packages.html)
* [Detecting Malicious SMB Activity Using Bro](https://www.sans.org/reading-room/whitepapers/detection/detecting-malicious-smb-activity-bro-37472)
* [MIME Types List](https://www.freeformatter.com/mime-types-list.html)
* [THREAT HUNTING WITH BRO](https://sqrrl.com/threat-hunting-bro/)
* [Binary Packages for Bro Releases](https://www.bro.org/download/packages.html) 
