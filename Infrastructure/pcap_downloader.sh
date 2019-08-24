for i in {001..536};
do
	# Download file via curl
	wget --user=<user> --password=<password> -r -nH -l10 -c -t0 --cut-dirs=4 https://ant.isi.edu/tracedist/LODHJBEPC/LODHJBEPC.data/dayone/dayone.$i.pcap.xz

	# Untar pcap
	unxz dayone.$i.pcap.xz

	# Analyze PCAP with BRO
    /opt/bro/bin/bro -Cr dayone.$i.pcap

	# Delete PCAP and xzz
	rm dayone.$i.*

	# Send Slack notification
	curl -X POST --data-urlencode "payload={\"channel\": \"#<channel>\", \"username\": \"webhookbot\", \"text\": \"PCAP $i done being processed.\", \"icon_emoji\": \":ghost:\"}" https://hooks.slack.com/services/<slack token>

done
