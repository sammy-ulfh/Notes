# Index

- [[#Users and Groups]]
  - [[#Substitute user]]
  - [[#super user do]]
  - [[#Add user]]
  - [[#Delete user]]
  - [[#Modify user settings]]
  - [[#Change password]]
  - [[#How to get user info]]
  - [[#How to add a user group]]
- [[#Nexto Notes]]

# Users and Groups

Each User in UNIX has the following parameters:

- User name
- Encrypted password (or 'x' if hash is stored)
- User identifier (UID)
- Group identifier (GID)
- Full name or description
- User's home directory
- User's shell
- Expiration date

Each group in UNIX has the following parameters:

- Group name
- Encrypted password (or 'x' if hash is stored)
- Group identifier (GID)

List of usernames for people who are members of this group By default in any UNIX created some users. Information about all users you can find in file __/etc/passwd__.

```
$ cat /etc/passwd
root:x:0:1:Super-User:/:/sbin/sh 
daemon:x:1:1::/: 
bin:x:2:2::/usr/bin: 
sys:x:3:3::/: 
adm:x:4:4:Admin:/var/adm: 
lp:x:71:8:Line Printer Admin:/usr/spool/lp: 
uucp:x:5:5:uucp Admin:/usr/lib/uucp: 
nuucp:x:9:9:uucp Admin:/var/spool/uucppublic:/usr/lib/uucp/uucico smmsp:x:25:25:SendMail Message Submission Program:/: 
listen:x:37:4:Network Admin:/usr/net/nls: 
nobody:x:60001:60001:Nobody:/:
```

User parameters:

![[user-param.png]]

Each user should belong to User group (at least one). Information about these groups you can find in __/etc/group__.

```
root::0:root 
other::1: 
bin::2:root,bin,daemon 
sys::3:root,bin,sys,adm 
adm::4:root,adm,daemon 
uucp::5:root,uucp 
mail::6:root 
tty::7:root,adm 
lp::8:root,lp,adm 
nuucp::9:root,nuucp 
staff::10:
```

Group parameters:

![[group-param.png]]

__root is super user. It has unlimited rights in the system.__

__Do not use without necessity!__

User:

- su
- sudo
- useradd
- userdel
- usermod
- passwd
- finger

Groups:

- groupadd
- groupdel
- groupmod
- groups

## Substitute user

__su__ - switch between users

> You shoud know password of user to which you want switch

```
# su - user or su user
# su
# su root
```


### super user do
__sudo__ - run programs with the security privileges of another user.

> Prompts for a current user password by default

```
# sudo ifconfig
# sudo su ---- the same as su but doesn’t require root password
```

### Add user

__useradd__ - create user (requires root acess)

```
# useradd –d /home/mydir –s /bin/bash user1
```

![[useradd.png]]

### Delete user

__userdel__ - delete user (requires root acess)

```
# userdel user - Delete user user
# userdel –r tester - Delete user tester with its home directory and files
```

### Modify user settings

__usermod__ - modify user account information (requires root acess)

```
# usermod -d /home/newhome user - modify the home directory for the user account to "/home/newhome"
```

### Change password

__passwd__ - change of user password

```
#passwd - command
april09 - current password
finalday - new password
finalday
```

### How to get user info

__finger__ - get user detailed info

```
# finger user
Login name: user
Directory: /home/myfolder 
Shell: /bin/bash
```

### How to add a user group

__groupadd__ - create new group

```
# groupadd mytestgroup - Create group “mytestgroup”
```

# Nexto Notes

[[Permission Model]]