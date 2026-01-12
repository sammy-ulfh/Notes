# Index

- [[#Firewall.d and IPtables]]
  - [[#Using Firewalls]]
  - [[#Comparison of firewalld to system-config-firewall and iptables]]
  - [[#Masquerading]]
  - [[#Port forwarding]]
- [[#Next Notes]]

# Firewall.d and IPtables

## Using Firewalls

The Firewall daemon provides a dynamically managed firewall with support for network "zones" to assign a level of trust to a network and its associated connections and interfaces. It has support for IPv4 and IPv6 firewall setting. It supports Ethernet bridges and IP set and has a separation of runtime and permanent configuration options. It also has an interface for services or applications to add firewall rules directly.

![[firewall.png]]

## Comparison of firewalld to system-config-firewall and iptables

The iptables service stores configuration in /etc/sysconfig/iptables and /etc/sysconfig/ip6tables, while firewalld stores it in various XML filres in /usr/lib/firewalld and /etc/firewalld. Note that the /etc/sysconfig/iptables file does not exist as firewalld is installed by default on Red Hat Enterprise Linux.

With the iptables service, every single change means flushing all the old rules and reading all the new rules from /etc/sysconfig/iptables, while with firewalld there is no recreating of all the rules. Only the differences are applied. Consequently, firewalld can change the settings during runtime without existing connections being lost.

__Firewalld zones__

- __drop__: The lowest level of trust. All incoming connections are dropped without reply and only outgoing connections are possible.
- __block__: Similar to the above, but instead of simply dropping connections, incoming requests are rejected with an icmp-host-prohibited or icmp6-adm-prohibited message.
- __public__: Represents public, untrusted networks. You don't trust other computers but may allow selected incoming connections on a case-by-case basis.
- __external__: External networks in the event that you are using the firewall as your gateway. It is configured for NAT masquerading so that your internal network remains private but reachable.
- __internal__: The other side of the external zone, used for the internal portion of a gateway . The computers are fairly trustworthy and some additional services are available.
- __dmz__: Used for computers located in a DMZ (isolated computers that will not have access to the rest of your network). Only certain incoming connections are allowed.
- __work__: Used for work machines. Trust most of the computers in the network. A few more services might be allowed.
- __home__: A home environment. It generally implies that you trust most of the other computers and that a few more services will be accepted.
- __trusted__: Trust all of the machines in the network. The most open of the available options and should be used sparingly

Firewall examples:
```
# firewall-cmd --get-services
cluster-suite pop3s bacula-client smtp ipp radius bacula ftp mdns samba dhcpv6-client dns openvpn imaps samba-client http https ntp vnc-server telnet libvirt ssh ipsec ipp-client amanda-client tftp-client nfs tftp libvirt-tls

# firewall-cmd --info-service=ftp
ftp
  ports: 21/tcp
  protocols: 
  source-ports: 
  modules: nf_conntrack_ftp
  destination:

# Dropping All Packets (Panic Mode)
# firewall-cmd --panic-on
# firewall-cmd --panic-off
```

## Masquerading

If your firewall is your network gateway and you don't wan everybody to know your internal addresses, you can set up two zones, one called internal, the other external, and configure masquerading on the external zone. This way, all packets will get your firewall ip address as source address. To set up masquerading on the external zone in a temporary way, type:

```
# firewall-cmd --zone=external --add-masquerade
success
```

> To remove masquerading, use the --remove-masquerade option.
> To know if masquerading is active in a zone, use the --query-masquerade option.
> To get the configuration permanent, add the --permanent option and reload the firewall configuration.

## Port forwarding

Port forwarding is a way to forward inbound network traffic for a specific port to another internal address or an alternative port.

> __Caution__ - Port forwarding requires masquerading (source). This point is a classical mistake made during the RHCE exam. If you want all packets intended for port 22 to be now forwarded to port tcp 3753 temporarily, type:

```
# firewall-cmd --zone=external --add-forward-port=port=22:proto=tcp:toport=3753
success
```

# Next Notes

[[Remote Access]]