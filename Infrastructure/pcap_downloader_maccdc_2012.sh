#!/bin/bash

# Slack token
slack_token=""
slack_channel=""

# Install software
apt install gunzip tcpreplay -y

# Make directory
mkdir ./maccdc2012
cd maccdc2012

for i in {00000..00016};
do
	# Download file via curl
    curl "https://download.netresec.com/pcap/maccdc-2012/maccdc2012_${i}.pcap.gz" \
    -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36' \
    -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-User: ?1' \
    -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' \
    -H 'Sec-Fetch-Site: same-site' -H 'Referer: https://www.netresec.com/?page=MACCDC' \
    -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9' -H 'dnt: 1' --compressed \
    --output maccdc2012_${i}.pcap.gz

	# Untar pcap
    gunzip maccdc2012_${i}.pcap.gz

	# Analyze PCAP with BRO
    /opt/zeek/bin/zeek -Cr maccdc2012_${i}.pcap /opt/zeek/share/zeek/site/local.zeek

	# Delete PCAP and xzz
	rm maccdc2012_${i}.*

	# Send Slack notification
	curl -X POST --data-urlencode "payload={\"channel\": \"#${slack_channel}\", \"username\": \"webhookbot\", \"text\": \"PCAP $i done being processed.\", \"icon_emoji\": \":ghost:\"}" https://hooks.slack.com/services/${slack_token}

done