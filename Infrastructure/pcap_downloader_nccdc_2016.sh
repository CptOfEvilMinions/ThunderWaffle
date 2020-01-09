#!/bin/bash

# Slack token
slack_token=""
slack_channel=""

# Make directory
mkdir ./nccdc2016
cd nccdc2016

# Create and mount RAM disk
mkdir /mnt/ramdisk
mount -t tmpfs -o size=2g tmpfs /mnt/ramdisk

for i in {000..542};
do
	# Download file via curl
	time curl "https://ant.isi.edu/tracedist/MB55gDB2i/MB55gDB2i.data/dayone/dayone.${i}.pcap" \
	-H 'Connection: keep-alive' -H 'Authorization: Basic <Base64 auth key>' \
	-H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36' \
	-H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-User: ?1' \
	-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' \
	-H 'Sec-Fetch-Site: same-origin' \
	-H 'Referer: https://ant.isi.edu/tracedist/MB55gDB2i/MB55gDB2i.data/dayone/' \
	-H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9' --compressed \
	--output /mnt/ramdisk/dayone.${i}.pcap

	# Analyze PCAP with BRO
	time /opt/zeek/bin/zeek -Cr /mnt/ramdisk/dayone.${i}.pcap /opt/zeek/share/zeek/site/local.zeek

	# Tracker
	sha1sum /mnt/ramdisk/dayone.${i}.pcap >> pcap_tracker_list.txt

	# Delete PCAP and xzz
	rm /mnt/ramdisk/dayone.$i.*

	# Append each JSON file to long_json
	for x in $(find * -name "*-json.log" ! -name "long_*" -type f -print); 
	do 
		cat ${x} >> long_${x};
		echo ${x}; 
	done

	# Send Slack notification
	curl -X POST --data-urlencode "payload={\"channel\": \"${slack_channel}\", \"username\": \"webhookbot\", \"text\": \"PCAP dayone.${i}.pcap done being processed.\", \"icon_emoji\": \":ghost:\"}" https://hooks.slack.com/services/${slack_token}
done