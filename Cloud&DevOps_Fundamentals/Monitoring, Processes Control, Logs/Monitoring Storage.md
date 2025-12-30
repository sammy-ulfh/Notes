# Index

- [[#Monitoring Storage]]
  - [[#DF]]
  - [[#DU]]
  - [[#LSOF]]
  - [[#VMSTAT]]
  - [[#IOSTAT]]
- [[#Next Notes]]

# Monitoring Storage

## DF

__df__ - show available drive space in the system

```
$ df –h
Filesystem      Size  Used Avail Use% Mounted on
rootfs          120G  109G   12G  91% /
none            120G  109G   12G  91% /dev
none            120G  109G   12G  91% /run
none            120G  109G   12G  91% /run/lock
none            120G  109G   12G  91% /run/shm
none            120G  109G   12G  91% /run/user
C:              120G  109G   12G  91% /c
E:              119G   49G   70G  42% /e
```

## DU

__du__ - show disk usage information for given folder

```
$du –sh /etc/*
4.0K    /etc/BUILDTIME
8.0K    /etc/DIR_COLORS
8.0K    /etc/DIR_COLORS.256color
8.0K    /etc/DIR_COLORS.lightbgcolor
4.0K    /etc/GREP_COLORS
20K     /etc/X11
4.0K    /etc/adjtime.rpmsave
4.0K    /etc/aliases
4.0K    /etc/alternatives
16K     /etc/bash_completion.d
```

## LSOF

__lsof__ - view a list of open files

In the absence of any options, lsof list all open files belonging to all active processes

```
$ lsof | less

$ lsof /usr/bin/sshd #listing of files for processes executing the command

$ lsof –c sshd #listing of files for processes executing the command

$ lsof -i #listing of all Internet and x.25 (HP-UX) network files (connections)
```

## VMSTAT

__vmstat__ - provides instant reports on your system's processes, memory, paging, block input/output, interrupts, and CPU activity.

```
$ vmstat –d # report disk statistics
disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda     8527     11  416987   19655   3189    460  751675  164139      0     15
dm-0    7585      0  367813   18899   3329      0  747499  167602      0     14
dm-1     128      0    2136     180      0      0       0       0      0      0

$ vmstat -p sda2 # detailed statistics about partition
sda2          reads   read sectors  writes    requested writes
                7802     371005       2626     747499
```

## IOSTAT

__iostat__ - monitors and reports on system input/output device loading.

```
$ iostat –t
Linux 3.10.0-514.10.2.el7.x86_64 (node11)     07/12/2020     _x86_64_    (2 CPU)

07/12/2020 09:27:09 PM
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.17    0.00    0.06    0.02    0.00   99.75

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.57        10.12        18.24     208569     375857
dm-0              0.53         8.93        18.13     183982     373769
dm-1              0.01         0.05         0.00       1068          0

$ iostat -d
Linux 3.10.0-514.10.2.el7.x86_64 (node11)     07/12/2020     _x86_64_    (2 CPU)

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.57        10.05        18.11     208569     375962
dm-0              0.53         8.86        18.01     183982     373874
dm-1              0.01         0.05         0.00       1068          0
```

# Next Notes

[[Logs]]