# Index

- [[#What is Shell?]]
- [[#Next Notes]]

# What is Shell?

The UNIX Shell program interprets user commands, which are either directly entered by the user, or which can be read from a file called the shell script or shell program.

Shell scripts are interpreted, not compiled.

The shell reads commands from the script line per line and searches for those commands on the system, while a compiles converts a program into machine readable form, en executable file - which may then be used in a shell script.

Apart from passing commands to the kernel, the main task of a shell is providing a user environment, which can be configured individually using shell resource configuration files.

The __/etc/shells__ give an overview of known shells on a Linux system:

```shell
$ cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/bin/dash
/usr/bin/dash
```

To switch from one shell to another, just enter the name of the new shell in the active terminal:

```shell
❯ ps --pid $$
    PID TTY          TIME CMD
   2462 pts/0    00:00:09 zsh
❯ bash
[sammy@sammy-pc ~]$ ps --pid $$
    PID TTY          TIME CMD
 358213 pts/0    00:00:00 bash
[sammy@sammy-pc ~]$ sh
sh-5.3$ ps --pid $$
    PID TTY          TIME CMD
 358381 pts/0    00:00:00 sh
```

# Next Notes

[[Shell type]]