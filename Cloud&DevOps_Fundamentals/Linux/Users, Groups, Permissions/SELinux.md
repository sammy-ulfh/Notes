# Index

- [[#SELinux modes]]
  - [[#SELinux Configuration File]]
  - [[#Enabling and Disabling SELinux]]
  - [[#Policies]]
- [[#Next Notes]]

# SELinux modes

Security Enhanced Linux or SELinux is an advanced access control mechanism built into most modern Linux distributions. SELinux implements what's known as MAC (Mandatory Access Control). This is implemented on top of what's already present in every Linux distribution, the DAC (Discretionary Access Control). At any one time, SELinux can be in any of three possible modes:

- Enforcing
- Permissive
- Disabled

In enforcing mode SELinux will enforce its policy on the Linux system and make sure any unauthorized access attemps by users and processes are denied. The access denials are also written to relevant log files. We will talk about SELinux policies and audit log later.

Permissive mode is like a semi-enabled state. SELinux doesn't  apply its policy in permissive mode, so no access is denied.
However any policy violation is still logged in the audit logs. It's a great way to test SELinux before enforcing it.

The disabled mode is self-explanatory - the system won't be running with enhanced security.

We can run the getenforce command to check the current SELinux mode.

`# getenforce`

SELinux should currently be disabled, so the output will look like this:

> Disabled

We can also run the status command:

`# sestatus`

When SELinux is disabled the output will show:

> SELinux status :               disabled


## SELinux Configuration File

The main configuration file for SELinux is __/etc/selinux/config__. We can run the following command to view its content:

```
$ cat /etc/selinux/config
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=disabled
# SELINUXTYPE= can take one of these two values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected. 
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted
```

## Enabling and Disabling SELinux

__Enable__

```
$ vi /etc/sysconfig/selinux
…
SELINUX=permissive
…
$ reboot
$ vi /etc/sysconfig/selinux file:
…
SELINUX=enforcing
…
```

__Disable__

```
$ vi /etc/sysconfig/selinux
…
SELINUX=disabled
…
$ reboot
```

## Policies

List the SELinux policy modules currently loaded into memory

```
$ semodule -l | less
abrt    1.2.0
accountsd       1.0.6
acct    1.5.1
afs     1.8.2
aiccu   1.0.2
aide    1.6.1
ajaxterm        1.0.0
alsa    1.11.4
amanda  1.14.2
amtu    1.2.3
anaconda        1.6.1
antivirus       1.0.0
apache  2.4.0
```

Changing SELinux Boolean Settings

```
$ semanage boolean -l | less
ftp_home_dir                   (off  ,  off)  Allow ftp to home dir
smartmon_3ware                 (off  ,  off)  Allow smartmon to 3ware
mpd_enable_homedirs            (off  ,  off)  Allow mpd to enable homedirs
xdm_sysadm_login               (off  ,  off)  Allow xdm to sysadm login
xen_use_nfs                    (off  ,  off)  Allow xen to use nfs
mozilla_read_content           (off  ,  off)  Allow mozilla to read content
ssh_chroot_rw_homedirs         (off  ,  off)  Allow ssh to chroot rw homedirs
mount_anyfile                  (on   ,   on)  Allow mount to anyfile
$ getsebool ftpd_anon_write
ftpd_anon_write --> off$ setsebool ftpd_anon_write on
$ getsebool ftpd_anon_write
ftpd_anon_write --> on
```


# Next Notes

[[Network Configuration]]