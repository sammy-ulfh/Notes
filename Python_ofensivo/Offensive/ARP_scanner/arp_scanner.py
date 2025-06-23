#!/usr/bin/env python3

import socket
import scapy.all as scapy
import argparse

def get_arguments():
    argparser = argparse.ArgumentParser(description="ARP Scanner Tool")
    argparser.add_argument("-t", "--target", required=True, dest="target", help="Host / Range target")

    args = argparser.parse_args()

    return args.target

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_packet = broadcast_packet/arp_packet

    answered, unanswered = scapy.srp(arp_packet, timeout=1, verbose=False)

    response = answered.summary()

    if response:
        print(response)

def main():
    target = get_arguments()
    scan(target)

if __name__ == "__main__":
    main()
