# ThunderWaffle
Repo for my Master's Thesis

# Setup infrastructure
## Setup Docker swarm
0. mv group_vars/all.example group_vars/all.yml
0. vim group_vars/all.yml and set:
    1. hostname - Set hostname for box
    1. base_domain - Set the domain for the box
    1. slack_channel - OPTIONAL - Set to Slack channel
    1. slack_token - OPTIONAL - Set to Slack channel token
0. mv group_vars/docker.example group_vars/docker.yml
0. vim group_vars/docker.yml and set:
    1. docker_path - Path for docker to store persistent data
        2. Default path `/srv/docker/<container>`
0. vim hosts.yml and under "[docker]" set:
    1. ansible_host - Set to IP addr of remote host
0. `ssh-copy-id <username>@<docker host>`
0. `ansible-playbook -i hosts.yml deploy_docker.yml -u <username> -K`

### Connect to Docker Swarm on Linux/MacOS
0. `docker-machine create --driver generic --generic-ip-address=<Docker IP addr> --generic-ssh-key ~/.ssh/id_rsa --generic-ssh-user=<username> <hostname>`
0. `eval $(docker-machine env <hostname>)`

## Setup Splunk server on Docker
0. mv group_vars/splunk.example group_vars/splunk.yml
0. vim group_vars/splunk.yml and set:
    1. splunk_forwarder_index
    1. splunk_server_addr
0. vim hosts.yml and under "[splunk]" set:
    1. ansible_host - Set to IP addr of remote host
0. `ansible-playbook -i hosts.yml deploy_splunk.yml -u <username> -K`
0. Browse "http://<Docker IP addr>:8000" and login
    1. Docker container runs an Ansible script which takes about ~2mins to run
    1. User: admin
    1. Pass: changeme

### Change password
0. Select the "Settings" tab at the top then "Acess Control" under "User and authentication"
0. Select "Users"
0. Select "Edit" under "Actions" for admin user
    1. Enter old password
    1. Enter new password
    1. Select "save"

### Adding Splunk input 
NOT required unless default port was changed
0. Select "Settings" then "Forwarding and receiving" under "Data"
0. Select "Configure receiving" under "Receive data"
0. Select "New Receiving port"
    1. Enter port number

### Create BRO index
0. Select "Settings" then "Indexes" under "Data"
0. Select "New index" in top right
0. Enter "bro" for Index name

### Adding Bro Add-on
0. https://splunkbase.splunk.com/app/1617/


## Setup Bro with splunk forwarder
### Setup Splunk
0. Open browser to "https://www.splunk.com/en_us/download" and login
0. Download latest splunk forwarder
0. Place splunkforwarder-*-amd64.deb inti files/splunk named as splunkforwarder.deb

### Setup Bro
0. mv group_vars/bro.example group_vars/bro.yml
0. vim group_vars/splunk.yml and set:
    1. bro_management_interface - Interface to access Bro box via SSH
    1. bro_promiscuous_interface - Interface to monitor network traffic
    1. bro_local_network - Local network that BRO is monitoring
    1. bro_mail_to - Location to send e-mails
0. vim hosts.yml and under "[bro]" set:
    1. ansible_host - Set to IP addr of remote host
0. `ansible-playbook -i hosts.yml deploy_bro.yml -u <username> -K`
    1. Be patient the make process may take 20+ mins

## Supported OSes
* Ubuntu Server 18.04 64-bit

## Resources/Sources
* http://derpturkey.com/setting-host-with-ansible-in-ubuntu/
* https://www.kevinkuszyk.com/2016/11/28/connect-your-docker-client-to-a-remote-docker-host/
* https://raw.githubusercontent.com/CptOfEvilMinions/GuardiansOfTheNetwork/master/Setup/roles/docker/setup_docker.yml
* https://www.splunk.com/en_us/download
* https://linoxide.com/linux-how-to/install-splunk-ubuntu/
* https://answers.splunk.com/answers/59662/is-there-a-systemd-unit-file-for-splunk.html
* https://undercoverelephant.info/2018/02/07/configuring-bro-for-splunk/