from scapy.all import *

pkt=sniff(iface='enp0s3',filter='icmp or udp',count=10)
pkt.summary()
