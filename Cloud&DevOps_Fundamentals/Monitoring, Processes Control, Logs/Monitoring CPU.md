# Index

- [[#Monitoring CPU]]
  - [[#LSCPU]]
  - [[#MPSTAT]]
  - [[#SAR]]
- [[#Next Notes]]

# Monitoring CPU

## LSCPU

__lscpu__ - gathers information about the CPU architecture, such as the number of CPUs, threads , cores, sockets , and NUMA nodes

```
# lscpu
Architecture:	x86_64
CPU op-mode(s):	32-bit, 64-bit
Byte Order:	Little Endian
CPU(s):	40
On-line CPU(s) list:	0-39
Thread(s) per core:	1
Core(s) per socket:	10
Socket(s):	4
NUMA node(s):	4
Vendor ID:	GenuineIntel
CPU family:	6
Model:	47
Model name:	Intel(R) Xeon(R) CPU E7- 4870  @ 2.40GHz
Stepping:	2
```

## MPSTAT

__mpstat__ - display CPU statistics of individual CPU (or) Core.

If no activity has been selected, then the default reports is the CPU utilization report. If no interval specified then processors statistics are to be reported for the time since system startup (boot).

```
# mpstat -P ALL
Linux 2.6.32-100.28.5.el6.x86_64 (dev-db)       07/09/2011      _x86_64_        (4 CPU)
10:28:04 PM	CPU  %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest   %idle
10:28:04 PM  all	0.00    0.00	0.00    0.00      0.00    0.00    0.00	0.00   99.99
10:28:04 PM    0	0.01    0.00	0.01    0.01      0.00    0.00    0.00	0.00   99.98
10:28:04 PM    1	0.00    0.00	0.01    0.00      0.00    0.00    0.00	0.00   99.98
10:28:04 PM    2	0.00    0.00	0.00    0.00      0.00    0.00    0.00	0.00  100.00
10:28:04 PM    3	0.00    0.00	0.00    0.00      0.00    0.00    0.00	0.00  100.00
```

## SAR

__sar__ - display CPU statistics of individual CPU (or) Core

```
# $ sar -P ALL 1 1
Linux 2.6.18-194.el5PAE (dev-db)        03/26/2011      _i686_  (8 CPU)
01:34:12 PM       CPU     %user     %nice   %system   %iowait    %steal     %idle
01:34:13 PM       all        11.69      0.00      4.71	0.69      0.00     82.90
01:34:13 PM         0        35.00      0.00      6.00	0.00      0.00     59.00
01:34:13 PM         1        22.00      0.00      5.00	0.00      0.00     73.00
01:34:13 PM         2        3.00        0.00      1.00	0.00      0.00     96.00
01:34:13 PM         3        0.00        0.00      0.00	0.00      0.00    100.00
```

# Next Notes

[[Monitoring Memory]]