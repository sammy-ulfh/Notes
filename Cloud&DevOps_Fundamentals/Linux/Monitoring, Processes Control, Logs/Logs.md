# Index

- [[#Logs]]
  - [[#DMESG]]
  - [[#What is journalctl?]]
- [[#Next Notes]]
# Logs

## DMESG

__dmesg__ - command on most Unix-like operating systems that prints the message buffer of the kernel.

```
$ dmesg -T
[Sun Jul 12 15:43:37 2020] Initializing cgroup subsys cpuset
[Sun Jul 12 15:43:37 2020] Initializing cgroup subsys cpu
[Sun Jul 12 15:43:37 2020] Initializing cgroup subsys cpuacct
[Sun Jul 12 15:43:37 2020] Linux version 3.10.0-514.10.2.el7.x86_64 (builder@kbuilder.dev.centos.org) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-11) (GCC) ) #1 SMP Fri Mar 3 00:04:05 UTC 2017
[Sun Jul 12 15:43:37 2020] Command line: BOOT_IMAGE=/vmlinuz-3.10.0-514.10.2.el7.x86_64 root=/dev/mapper/cl-root ro crashkernel=auto rd.lvm.lv=cl/root rd.lvm.lv=cl/swap rhgb quiet LANG=en_GB.UTF-8
[Sun Jul 12 15:43:37 2020] e820: BIOS-provided physical RAM map:
[Sun Jul 12 15:43:37 2020] BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable
[Sun Jul 12 15:43:37 2020] BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved
[Sun Jul 12 15:43:37 2020] BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved
[Sun Jul 12 15:43:37 2020] BIOS-e820: [mem 0x0000000000100000-0x000000003ffeffff] usable
```

## What is journalctl?

- In modern Linux systems logging subsystem is implemented by __systemd-journald__. It's a system service that collects and stores logging data.
- It creates and maintains structured, indexed binary files called journals based on logging information that is receive from a variety of sources.
- One of the impetuses behind the systemd journal is to centralize the management of logs regardless of where the messages are originating.
- __journalctl__ is a utility to query and display the systemd journal data.

```
# journalctl -u httpd
-- Logs begin at Sun 2019-09-22 20:11:33 UTC, end at Sun 2019-09-22 20:11:39 UTC. --
Sep 22 20:11:33 97105f929c3b systemd[1]: Starting The Apache HTTP Server...
Sep 22 20:11:33 97105f929c3b httpd[147]: AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.17.0.2. Set the 'ServerName' direc
tive globally to suppress this message
Sep 22 20:11:33 97105f929c3b systemd[1]: Started The Apache HTTP Server.
```

To show only entries logged at the error level or above, you can type:

```
$ journalctl -p err –b –x
...
```

Where:

__-p__ means priority or log level
__-b__ means since last boot
__-x__ means to add explanatory help texts to log messages in the output where this is available. These short help texts will explain the context of an error or log event, possible solutions, as well as pointers to support forums, developer documentation, and any other relevant humans.

To show only entries for specified syslog identifier:

```
$ journalctl -t dockerd
-- Logs begin at Fri 2020-03-13 13:17:01 +03, end at Sun 2020-04-26 11:40:10 +03. --
Mar 16 14:23:56 localhost dockerd[2009]: time="2020-03-16T14:23:56" level=info msg="ignoring event" modu...
Mar 16 14:25:04 localhost dockerd[2009]: time="2020-03-16T14:25:04" level=info msg="ignoring event" modu...
Mar 16 14:31:59 localhost dockerd[2009]: time="2020-03-16T14:31:59" level=info msg="parsed scheme: \"\""...
Mar 16 14:31:59 localhost dockerd[2009]: time="2020-03-16T14:31:59" level=info msg="scheme \"\" not regi...
Mar 16 14:31:59 localhost dockerd[2009]: time="2020-03-16T14:31:59" level=info msg="ccResolverWrapper: s...
Mar 16 14:31:59 localhost dockerd[2009]: time="2020-03-16T14:31:59" level=info msg="ClientConn switching...
```

To see messages logged within a specific time window, we can use the --since and --until options.

```
$ journalctl --since "1 hour ago"
…
$ journalctl --since "2 days ago"
…
$ journalctl --since "2015-06-26 23:15:00" --until "2015-06-26 23:20:00"
…
```

- __/var/log/messages__ - Contains global system messages, including the messages that are logged during system startup. There are several things that are logged in __/var/log/messages__ including mail, cron, daemon, kern, auth, etc.
- __/var/log/secure__ - Contains information related to authentication and authorization privileges. For example, sshd logs all the messages here, including unsuccessful login.
- __/var/log/cron__ - Whenever cron daemon (or anacron) starts a cron job, it logs the information about the cron job in this file.
- __/var/log/auth.log__ - Contains system authorization information, including user logins and authentication machinsm that were used.
- __/var/log/maillog /var/log/mail.log__ - Contains the log information from the mail server that is running on the system. For example, sendmail logs information about all the sent items to this file.
- __/var/log/mail__ - This subdirectory contains additional logs from your mail server.
- __/var/log/sa__ - Contains the daily sar files that are collected by the sysstat package.

# Next Notes

[[What is Shell]]