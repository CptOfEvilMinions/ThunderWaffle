# Infrastructure

## Init setup

1. `mv group_vars/all.example group_vars/all.yml`
1. `vim group_vars/all.yml` and set:
    1. `hostname` - Set hostname for box
    1. `base_domain` - Set the domain for the box
    1. `Cert generation`- Insert values
    1. `slack_channel` - OPTIONAL - Set to Slack channel
    1. `slack_token` - OPTIONAL - Set to Slack channel token

### Setup Docker swarm

1. `mv group_vars/docker.example group_vars/docker.yml`
1. `vim group_vars/docker.yml` and set:
    1. `docker_path` - Path for docker to store persistent data
        1. Default path `/srv/docker/<container>`
1. `vim hosts.yml` and under "[docker]" set:
    1. ansible_host - Set to IP addr of remote host
1. `ssh-copy-id <username>@<docker host>`
1. `ansible-playbook -i hosts.yml deploy_docker.yml -u <username> -K`
    1. `-K` will prompt for user's password

#### Connect to Docker Swarm on Linux/MacOS

1. `docker-machine create --driver generic --generic-ip-address=<Docker IP addr> --generic-ssh-key ~/.ssh/id_rsa --generic-ssh-user=<username> <hostname>`
1. `eval $(docker-machine env <hostname>)`

### Setup Splunk server on Docker

1. `mv group_vars/splunk.example group_vars/splunk.yml`
1. `vim group_vars/splunk.yml` and set:
    1. `splunk_forwarder_index` - Index to store bro logs
    1. `splunk_server_addr` - IP addr of Splunk
    1. `splunk_server_password` - Password for Splunk server webGUI login
1. vim hosts.yml and under "[splunk]" set:
    1. ansible_host - Set to IP addr of remote host
1. `ansible-playbook -i hosts.yml deploy_splunk.yml -u <username> -K`
1. Browse `https://<Docker IP addr>` and login
    1. Docker container runs an Ansible script which takes about ~2mins to run
    1. User: admin
    1. Pass: `<splunk_server_password>`

#### Change password

1. Select the "Settings" tab at the top then "Acess Control" under "User and authentication"
1. Select "Users"
1. Select "Edit" under "Actions" for admin user
    1. Enter old password
    1. Enter new password
    1. Select "save"

#### Create BRO index

1. Select "Settings" then "Indexes" under "Data"
1. Select "New index" in top right
1. Enter "bro" for Index name

#### Adding Bro Add-on

1. https://splunkbase.splunk.com/app/1617/

### Setup Bro with splunk forwarder

#### Setup Splunk

1. Open browser to `https://www.splunk.com/en_us/download` and login
1. Download latest splunk forwarder
1. Place splunkforwarder-*-amd64.deb inti files/splunk named as splunkforwarder.deb

#### Setup Bro

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

## Supported OSes

* Ubuntu Server 18.04 64-bit

## Resources/Sources

### Ansible

* [Setting hostname with Ansible](http://derpturkey.com/setting-host-with-ansible-in-ubuntu/)

### Docker

* [Connect your Docker client to a remote Docker host](https://www.kevinkuszyk.com/2016/11/28/connect-your-docker-client-to-a-remote-docker-host/)
* [Github - Setup Docker](https://raw.githubusercontent.com/CptOfEvilMinions/GuardiansOfTheNetwork/master/Setup/roles/docker/setup_docker.yml)

### Splunk

* [Splunk Download](https://www.splunk.com/en_us/download)
* [How to Install Splunk on Ubuntu 18.04](https://linoxide.com/linux-how-to/install-splunk-ubuntu/)
* [Splunk SystemD file](https://answers.splunk.com/answers/59662/is-there-a-systemd-unit-file-for-splunk.html)

### Bro

* [Confiure Bro for Splunk](https://undercoverelephant.info/2018/02/07/configuring-bro-for-splunk/)