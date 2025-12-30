# Index

- [[#Network Configuration]]
  - [[#ifconfig]]
  - [[#Configuring a Network Interface Using __ip__ command]]
  - [[#Configuring Static Routes Using the Command Line]]
  - [[#Configuring a Network Interface Using __ip__ Command]]
  - [[#Default Gateway]]
  - [[#Red Hat Based]]
  - [[#Debian Based]]
- [[#Next Notes]]

# Network Configuration

## ifconfig

__ifconfig__ - configure and control TCP/IP network interfaces

You can install this command by installing __net-tools__ package.

Common uses for __ifconfig__ include

- setting and interface's IP address and netmask
- disabling or enabling a given interface

```
# ifconfig - displaying the current state of network interfaces

# ifconfig –a - display all interfaces which are currently available, even if down

# ifconfig eth0 - displaying the current state of eth0 interface

# ifconfig eth0 up - - Activating and deactivating eth0 interface
```

## Configuring a Network Interface Using __ip__ command

Assigning a Static Address Using ip:

```
# ip address add 192.168.2.223/24 dev eth1
# ip address add 192.168.4.223/24 dev eth1
# ip addr show dev eth1
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether 52:54:00:fb:77:9e brd ff:ff:ff:ff:ff:ff
    inet 192.168.2.223/24 scope global eth1
    inet 192.168.4.223/24 scope global eth1
```

## Configuring Static Routes Using the Command Line

```
# ip route add 192.0.2.1 via 10.0.0.2 dev eth0
# ip route add 192.0.2.0/24 via 10.0.0.3 dev eth0
# ip route
default via 10.0.0.10 dev ens9  proto static  metric 1024
192.168.122.0/24 dev ens9  proto kernel  scope link  src 10.0.0.1
192.168.122.0/24 dev eth0  proto kernel  scope link  src 10.0.0.1
192.0.2.1/32 dev eth0  proto kernel  scope link  src 10.0.0.2
192.0.2.0/24 dev eth0  proto kernel  scope link  src 10.0.0.3
```

## Configuring a Network Interface Using __ip__ Command

### Default Gateway

The default Gateway is determined by the network scripts which parse the __/etc/sysconfig/network__ file first and then the network interface ifcfg files for interfaces that are __up__. The __ifcfg__ files are parsed in numerically ascending order, and the last GATEWAY directive to be read is used to compose a default route in the routing table.

The default route can thus be indicated by meas of the GATEWAY directive, either globally or in interface-specific configuration files. However, in Red Hat Enterprise Linux the use of the global __/etc/sysconfig/network__ file is deprecated, and specifying the gateway should now only be done in per-interface configuration files.

```
# service network restart
Shutting down interface eth0:                              [  OK  ]
Bringing up interface eth0:
Determining IP information for eth0... done.          [  OK  ]
```


## Red Hat Based

- __/etc/sysconfig/network-scripts/ifcfg-ethX__
- __/etc/sysconfig/network__
- __/etc/resolv.conf__

```
[root@rhel ~]# cat /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
IPADDR=208.164.186.1
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
ONBOOT=yes
BOOTPROTO=dhcp

[root@rhel ~]# cat /etc/sysconfig/network
NETWORKING=yes
HOSTNAME=myhost.local
```

## Debian Based

- __/etc/network/interfaces__
- __/etc/hostname__
- __/etc/resolv.conf__

```
root@ubuntu:~# cat /etc/network/interfaces
auto lo eth0
iface eth0 inet static 
address 192.168.0.10
netmask 255.255.255.0
gateway 192.168.0.1

root@ubuntu:~# cat /etc/hostname
myhost.local
```

The Name Service Switch (NSS) is a facility in Unix-like operating systems that provides a variety of sources for common configuration databases and name resolution mechanism. These sources include local operating system files (such as /etc/passwd, /etc/group, and /etc/hosts), the Domain Name System (DNS), the Networking Information Service (NIS), and LDAP. Files specifies that the local file should be used, db specifies a database lookup, and dns specifies that a DNS server should be consulted. The order in which you  list these keywords determines the order in which the data source are searched.

```
# cat /etc/nsswitch.conf
passwd:		files ldap
shadow:		files
group:		files ldap
hosts:		dns nis files
ethers:		files nis
netmasks:	files nis
networks:	files nis
protocols:	files nis
rpc:		files nis
services:	files nis
automount:	files
aliases:	files
```

# Next Notes

[[Networking Tools]]