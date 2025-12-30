# Index

- [[#Monitoring Memory]]
  - [[#Free]]
  - [[#VMSTAT]]
- [[#Next Notes]]

# Monitoring Memory

## Free

__free__ - show information about operating system memory

```
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           992M         78M        324M        6.8M        590M        746M
Swap:          2.0G         70Mi       1.9G
```

## VMSTAT

__vmstat__ - provides instant reports on your system's processes, memory, paging, block input/output, interrupts, and CPU activity.

vmstat lets you set a sampling interval so that you can observe system activity in near-real time.

```
$ vmstat -a
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
r  b   swpd   free  inact active   si   so    bi    bo   in   cs us sy id wa st
1  0      0 332128  85800 505656    0    0     5    10   13   17  0  0 100  0  0

$ vmstat -f
        11703 forks #total number  of  tasks  created since last boot.

# vmstat -w 1 3
# vmstat -s
```

# Next Notes

[[Monitoring Storage]]