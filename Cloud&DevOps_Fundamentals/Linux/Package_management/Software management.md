# Index

- [[#Software management]]
  - [[#Red Hat Based]]
  - [[#Debian Based]]
  - [[#APT-GET]]
- [[#Next Notes]]

# Software management

A software package refers to computer software packaged in an archive format to be installed by a package management system or a self-sufficient installer.

A package management system is a collection of tools to automate the process of installing, upgrading, configuring, and removing software packages from a computer.

## Red Hat Based

- __\*.RPM__
- __rpm__
- __yum__

## Debian Based

- __\*.DEB__
- __dpkg__
- __apt__


- __RPM__ (Red Hat Package Manager) is a package management system. Originally developed by Red Hat or Red Hat Linux, RPM is nuw used by many Linux distributions.

- __YUM__ (The Yellow dog Updater, Modified) is an open source command line package management utility for RPM-compatible Linux operating systems and has been released under the GNU GPL.

- __deb__ is the extension of the Debian software package format and the most often used name for such binary packages. Like the "Deb" part of the term Debian, it originates from the name of Debra, then girlfriend and now ex-wife of Debian's founder Ian Murdock.

- __APT__, or The Advanced Packaging Tool, is a free user interface that works with core libraries to handle the installation and removal of software on the Debian GNU/Linux distribution and its variants.

## APT-GET

__apt-get__ - is a simple command line interface for downloading and installing packages. The most frequently used commands are update and install.

- __update__ - Retrieve new lists of packages
- __upgrade__ - Perform an upgrade
- __install__ - Install new packages (pkg is libc6 not libc6.deb)
- __remove__ - Remove packages
- __purge__ - Remove packages and config files
- __check__ - Verify that there are no broken dependencies 

__apt-cache__ - is a low-level tool used to manipulate API's binary cache files, and query information from them.

- __showpkg__ - Show some general information for a single package
- __search__ - Search the package list for a regex pattern
- __show__ - Show a readable record for the package
- __depends__ - Show raw dependency information for package

All of this packages are downloaded from repositories that are constantly updated. You can find them here:

```
$ ls /etc/apt/sources.list /etc/apt/sources.list.d/
/etc/apt/sources.list

/etc/apt/sources.list.d/:
docker-ce.list      kubernetes.list        winehq.list
gns3.list           terraform.list         aws.list

$ cat /etc/apt/sources.list
deb http://ftp.by.debian.org/debian/ buster main non-free contrib
deb-src http://ftp.by.debian.org/debian/ buster main non-free contrib

deb http://security.debian.org/debian-security buster/updates main contrib non-free
deb-src http://security.debian.org/debian-security buster/updates main contrib non-free

# buster-updates, previously known as 'volatile'
deb http://ftp.by.debian.org/debian/ buster-updates main contrib non-free
deb-src http://ftp.by.debian.org/debian/ buster-updates main contrib non-free

deb http://deb.debian.org/debian buster-backports main contrib non-free
```

# Next Notes

[[Alternatives]]