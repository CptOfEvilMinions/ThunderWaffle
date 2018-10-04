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
0. vim hosts.yml and set:
    1. ansible_host - Set to IP addr of remote host
0. `ssh-copy-id <username>@<docker host>`
0. `ansible-playbook -i hosts.yml deploy_docker.yml -u <username> -K`

### Connect to Docker Swarm on Linux/MacOS
0. `docker-machine create --driver generic --generic-ip-address=<Docker IP addr> --generic-ssh-key ~/.ssh/id_rsa --generic-ssh-user=<username> <hostname>`
0. `eval $(docker-machine env <hostname>)`

## Setup Splunk server on Docker
0. 

## Setup Bro with splunk forwarder
0.

## Supported OSes
* Ubuntu Server 18.04 64-bit

## Resources/Sources
* http://derpturkey.com/setting-host-with-ansible-in-ubuntu/
* https://www.kevinkuszyk.com/2016/11/28/connect-your-docker-client-to-a-remote-docker-host/
* https://raw.githubusercontent.com/CptOfEvilMinions/GuardiansOfTheNetwork/master/Setup/roles/docker/setup_docker.yml
