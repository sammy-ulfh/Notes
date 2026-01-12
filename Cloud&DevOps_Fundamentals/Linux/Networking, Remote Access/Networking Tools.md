# Index

- [[#Networking tools]]
  - [[#NSLOOKUP]]
  - [[#NETSTAT]]
  - [[#WHOIS]]
  - [[#TCPDUMP]]
- [[#Next Notes]]

# Networking tools

```
$ ping google.com      - sending a ping request 
$ ping –c 5 google.com

$ traceroute google.com - - show the network route for a given host
$ tracepath ya.ru

$ host ya.ru - translate ip address to hostname or vice versa
$ host 213.180.204.8

$ dig ya.ru - Another method
$ dig –x 213.180.204.8
```

## NSLOOKUP

__nslookup__ - a program to query Internet domain name services

DNS Lookups:

```
# nslookup epam.com
Server:		    10.99.158.150
Address:		10.99.158.150#53

Non-authoritative answer:
Name:		    epam.com
Address:		174.128.60.201
```

Reverse DNS Lookup:

```
# nslookup 174.128.60.201
Server:		    10.99.158.150
Address:		10.99.158.150#53

Non-authoritative answer:
201.60.128.174.in-addr.arpa     name = epam.by.
201.60.128.174.in-addr.arpa     name = epam.com.
201.60.128.174.in-addr.arpa     name = epam.mx.
```

## NETSTAT

__netstat__ - Display network connections, routing tables, interface statistics, masquerade connections, netlink messages, and multicast memberships

Example:

```
# netstat -ant
tcp        0      0 127.0.1.1:53		0.0.0.0:*		LISTEN     
tcp        0      0 127.0.0.1:631		0.0.0.0:*		LISTEN     
tcp        0      0 192.168.1.2:49058	173.255.230.5:80	ESTABLISHED
tcp6       0      0 ::1:631		:::*		LISTEN

# sudo netstat -nlpt
tcp        0      0 127.0.1.1:53		0.0.0.0:*		LISTEN      1144/dnsmasq    
tcp        0      0 127.0.0.1:631		0.0.0.0:*		LISTEN      661/cupsd       
tcp6       0      0 ::1:631		:::*		LISTEN      661/cupsd
```

## WHOIS

__whois__ - utility looks up records in the databases maintained by several Network Information Centers (NICs)

Example:

```
# whois google.com
Registrant:
        Dns Admin
        Google Inc.
        Please contact contact-admin@google.com 1600 Amphitheatre Parkway
         Mountain View CA 94043
        US
        dns-admin@google.com +1.6502530000 Fax: +1.6506188571
    Domain Name: google.com
    Created on..............: 1997-09-15.
    Expires on..............: 2020-09-13.
    Record last updated on..: 2012-01-29.
```

## TCPDUMP

__tcpdump__ - prints out a description of the contents of packets on a network interface that match the boolean expression.

Example:

```
# tcpdump -i eth0 - Basic view of what’s happening on a particular interface.
# tcpdump host 1.2.3.4 - Show you traffic from 1.2.3.4, whether it’s the source or the destination.
# tcpdump port 80 -w capture_file - Show you traffic on port 80 and write into capture_file
# tcpdump 'src 10.0.2.4 and (dst port 3389 or 22)' - # tcpdump 'src 10.0.2.4 and (dst port 3389 or 22)' - Traffic that comess from 10.0.2.4 AND destined for ports 3389 or 22 (correct)
```

# Next Notes

[[Firewall.d and IPtables]]