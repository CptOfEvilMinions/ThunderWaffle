# Setup Rsyslog

## Install/Setup Rsyslog

1. `mv group_vars/logging.example group_vars/logging.yml`
1. `vim group_vars/splunk.yml` and set:
    1. `rsyslog_port` - Port for Rsyslog to ingest logs on
    1. `rsyslog_tls` - Enable TLS - On by default
1. vim hosts.yml and under "[splunk]" set:
    1. ansible_host - Set to IP addr of remote host
1. `ansible-playbook -i hosts.yml deploy_rsyslog.yml -u <username> -K`
    1. `-K` will prompt for user's password

## Resources/Sources

### Rsyslog

* [How to ship JSON logs via Rsyslog](https://techpunch.co.uk/development/how-to-shop-json-logs-via-rsyslog)
* [Github - Go-Audit](https://github.com/slackhq/go-audit/blob/master/examples/rsyslog/rsyslog.conf)
* [Rsyslog - Parse Json and enrich IP with Geolocation using Maxmind GeoLite2 City and ISP](https://manios.org/2018/08/18/logstash-geoip-json-logs-maxmint-geolite-docker)