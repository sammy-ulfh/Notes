# Index

- [[#Service Management in Linux init.d and systemd]]
  - [[#init.d]]
  - [[#Basic syntax]]
  - [[#Example]]
  - [[#[Unit] Section]]
  - [[#[Service] section]]
  - [[#[Install] Section]]
- [[#Next Notes]]

# Service Management in Linux: init.d and systemd

Modern Linux distributions use systemd as the default init system and service manager. However, many systems still support legacy init.d scripts for backward compatibility. This section compares both approaches and shows how to create and manage services with each.

## init.d

__init.d__ is a legacy system used in Unix-like operating systems to manage services through shell scripts stored in the __/etc/init.d/__ directory. Each script defines how a particular service should start, stop or restart, using standardized command-line arguments like __start__, __stop__, and __restart__. These scripts were executed during system boot and shutdown sequences.

Though widely used in the past, __init.d__ has largely been replaced by __systemd__ in modern Linux distributions.

### Basic syntax

The init.d directory contains a number of shell scripts used to start and stop system services. These scripts are part of the traditional SysV-style init system.

Basic syntax for the init.d system is:

`/etc/init.d/<command> <options>`

Where:

- \<command> - there service name or script name
- \<option> - the operation to perform:
  - __start__
  - __stop__
  - __reload__
  - __restart__
  - __force-reload__

### Example

This script configures static network routes via defined gateway

```bash
# cat /etc/init.d/static_routes
#!/sbin/sh 
# Add static routes
GW=10.204.223.1
case "$1" in 'start’)       
  /usr/sbin/route add -net 10.204.0.0 -netmask 255.255.0.0 $GW        
  /usr/sbin/route add -net 10.200.0.0 -netmask 255.255.0.0 $GW        
  exit 0        
;;'stop’)
   exit 0
;; *)
   echo "Usage: $0 { start | stop }"
   exit 1
;;
esac
```

## Systemd

__systemd__ is a modern system and service manager for Linux operating systems. When running as a system instance, it reads configuration from __system.conf__ and files in __the system.conf.d__ directory. As a user instance, it reads from __user.conf__ and __user.conf.d__.

More than just an init daemon, __systemd__ refers to a broader suite of tools that includes core components like __journald__ (logging), __logind__ (user session management), and __networkd__ (network configuration), among others.

One key feature of systemd is the use of targets (__.target__), which group related units and serve as synchronization points during system startup. These targets are a flexible replacement for traditional SysV runlevels. However, for backward compatibility, targets like runlevel3.target still exist.

![[targets.png]]

__systemd Unit File Locations and resource types__

Unlike the order __init.d__ approach that uses per-service shell scripts, __systemd__ uses unit files written in a declarative syntax to define how each service should be initialized and managed.

These files are placed in:

- __/usr/lib/systemd/system/__ - Unit files provided by RPM-based packages (nginx, apache, mysql)
- __/run/systemd/system/__ - Unit files created at runtime
- __/etc/systemd/system/__ - user created Unit files

systemd unit files control different types of system resources. Common types include:

- __service__ - for system services (daemons)
- __socket__ - for socket activation
- __device__ - for device units
- __mount__, __automount__ - for filesystem mount
- __swap__ - for swap space
- __target__ - for grouping units and managing boot stages
- __path__ - for path-based activation
- __timer__ - for scheduled tasks (cron-like behavior)
- __snapshot__, __slice__, __scope__ - for advanced resource management

__Unit file syntax__

> For a full list of parameters and their descriptions, run `man systemd.unit` or visit [systemd.unit](https://man7.org/linux/man-pages/man5/systemd.unit.5.html) page.

Systemd unit files follow an .ini-like format, organized into three main sections - \[Unit], \[Service] and \[Install]

### \[Unit] Section

This section defines metadata and dependencies for the unit:

- __Description\=__ - a huma-readable summary of the unit's purpose
- __Documentation\=__ - references to man pages or URL's
- __Requires\=__ - strong dependency; if listed units fail, this one fails too
- __Wants\=__ - weaker dependency; listed units are started but no required to succeed
- __BindsTo\=__ - if the bound unit stops, this one stops as well
- __PartOf\=__ - stopping or restarting the listed units will also stop or restart this one
- __Conflicts\=__ - units that cannot be active simultaneously with this one
- __Before\=__ - this unit starts before the specified ones
- __Aftes\=__ - this unit starts after the specified ones
- __OnFailure\=__ - units to start if this one fails


### \[Service] section

This section carries information about the service and the process it supervises.

- __Type\=__ - defines the startup behavior (simple, forking, oneshot, notify)
- __ExecStart\=__ - command to start the service
- __ExecStartPre\=__ - command(s) to run before ExecStart
- __ExecStartPost\=__ - command(s) to run after ExecStart
- __ExecReload\=__ - command to reload service
- __ExecStop\=__ - command to stop service
- __Restart\=__ - behavior when the service fails or exits
- __PIDFile\=__ - path to a file storing the service's PID
- __User\=__ - user to run the service under
- __Group\=__ - group to run the service under
- __WorkingDirectory\=__ - sets the working directory for the service process
- __Environment\=__ - environment variables defined inline
- __EnvironmentFile\=__ - path to file containing environment variable definitions

### \[Install] Section

This section defines how the unit should be enabled or disabled.

- __WantedBy\=__ - targets that want this unit enabled
- __RequiredBy\=__ - targets that require this unit to be enabled
- __Alias\=__ - additional names for this unit
- __Also\=__ - other units to install/uninstall with this one

__Example__

This `tomcat.service` unit file defines how to manage the Tomcat application server using systemd:

```
$ cat /etc/systemd/system/tomcat.service
[Unit]
Description=Tomcat Application server
After=network.target

[Service]
Type=forking
ExecStart=/apps/tomcat/bin/startup.sh
ExecStop=/apps/tomcat/bin/shutdown.sh
User=tomcat55
Group=staff

[Install]
WantedBy=multi-user.target
```

```
# systemctl start [name.service]
# systemctl stop [name.service]
# systemctl restart [name.service]
# systemctl reload [name.service]
# systemctl status [name.service]
# systemctl is-active [name.service]
# systemctl list-units --type service --all
```

# Next Notes

[[Crond]]