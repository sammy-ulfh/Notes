#!/usr/bin/env python3

from mitmproxy import http

def response(packet):

    headers = packet.response.headers.get("content-type", "").split('/')
    ext = "jpg" if headers[-1] == "jpeg" else headers[-1]

    if "image" in headers:
        try:
            name = packet.request.url.replace('/', '_').replace(':', '_')
            content = packet.response.content

            if content:
                with open(f"images/{name}.{ext}", "wb") as f:
                    f.write(content)

                print("\n[+] Image Saved.")
        except:
            pass
