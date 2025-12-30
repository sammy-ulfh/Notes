# Index

- [[#Remote Access]]
  - [[#Console]]
  - [[#Protocols]]
  - [[#Programs]]
  - [[#X-System]]
  - [[#SSH Key Generation]]
  - [[#SSH Command]]
  - [[#SSH Access]]
  - [[#SSH Remote Command]]
  - [[#SCP]]
  - [[#Bation/SSh-proxy-command]]
  - [[#SSH Config File]]
  - [[#SFTP/FTP]]
- [[#Next Notes]]

# Remote Access

## Console

### Protocols

- Telnet
- SSH (Encrypted)

### Programs

- SSH
- WinSCP (offers basic file manager functionality, suitable for remote file copying)

### X-System

- X-System (server and client) uses client-server model and network-transparently protocol, can be used remotely
- Using VNC server/client software

## SSH Key Generation

```
# cd ~
# ssh-keygen -t rsa
Enter file in which to save the key (/home/user/.ssh/id_rsa):
Created directory '/home/user/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
* Can be empty
Your identification has been saved in /home/user/.ssh/id_rsa.
Your public key has been saved in /home/user/.ssh/id_rsa.pub.
The key fingerprint is: 
7e:f5:7e:51:ec:3d:2c:36:02:9d:5b:89:4a:3a:b7:b5 Linux Key
* Never distribute your private key to anyone.

# chmod 600 ~/.ssh/id_rsa
```

## SSH Command

- __-i__ key file location
- __-l__ login_name. Specifies the user to log in as on the remote machine.
- __-p__ port. Port to connect on the remote host.
- __-t__ Force pseudo-terminal allocation. This can be used to execute arbitrary screen-based programs on a remote machine, which can be very useful, when implementing menu services. Multiple -t options force tty allocation, even if ssh has no local tty.
- __-v__ verbose mode.
- __-N__ Do not execute a remote command. This is useful for just forwarding ports.

## SSH Access

Copy the contents of ~/.ssd/id_rsa.pub into the file ~/.ssh/authorized_keys on the machine to which you want to connect. If the file ~/.ssh/authorized_keys exists, append the content of the file ~/.ssh/id_rsa.pub to the file ~/.ssh/authorized_keys on the other machine.

```
$ ssh -i ~/.ssh/lab.pem centos@ecsc00a058b0.epam.com

Last login: Thu Aug 22 13:33:34 2019 from 10.6.207.129
[centos@ecsc00a058b0 ~]$
```

> ssh to user root os forbidden by default on most systems and has to be configured in /etc/ssh/sshd_config with sshd service restart


## SSH Remote Command

```
#Single command 
$ ssh centos@ecsc00a058b0.epam.com whoami
#Multiple commands
$ ssh centos@ecsc00a058b0.epam.com whoami; pwd; ls
#Sudo command - sudo requires interactive shell, it can be enabled with -t parameter.
$ ssh -t centos@ecsc00a058b0.epam.com sudo ls /root
#Local script execution 
$ ssh centos@ecsc00a058b0.epam.com < script.sh
```

## SCP

The __scp__ command allows you to copy files over ssh connections. This is pretty useful if you want to transport files between computers, for example backup something. The scp command uses the ssh command and they are very much alike.

```
$ scp examplefile centos@ecsc00a058b0.epam.com:/folder
$ scp centos@ecsc00a058b0.epam.com:/home/yourusername/examplefile .
$ scp centos@ecsc00a058b0.epam.com:/examplefile \
root@ecsc00a058b9.epam.com:/home/user/
```

## Bation/SSh-proxy-command

Bastion hosts are instances that sit within your public subnet and are typically accessed using SSH (for Linux) or RDP (for Windows). It acts as a __jump__ server, allowing you to use SSH or RDP to login to other instance in private subnet. Ssh access through bastion host/jumpserver.

```
$ ssh -i ~/.ssh/lab.pem -o "ProxyCommand ssh -W %h:%p -i key_for_jumpbox.pem jumpbox_user@jump.box.host" centos@ecsc00a058b0.epam.com
```

## SSH Config File

If you are regularly connecting to multiple remote systems over SSH on a daily basis, you'll find that remembering all of the remote IP addresses, different usernames, non standard ports and various command line options is difficult, if not impossible.

OpenSSH allows you to set up per-user configuration file where you can store different SSH options for each remote machine you connect to. Create ssh config file.

```
$ touch ~/.ssh/config && chmod 600 ~/.ssh/config
#Connecting to hosts specified in config file
$ ssh targaryen
#Will be equal to
$ ssh -i ~/.ssh/targaryen.key -p 7654 daenerys@192.168.1.10
```

## SFTP/FTP

- main function is secure file transfer between a local and remote computer
- Support for SFTP and SCP protocols over SSH-1 and SSH-2 and plain old FTP protocol
- Batch File scripting and command-line interface
- Integrated text editor
- Directory synchronization in several semi or fully automatic ways, etc.

```
sftp access@192.168.0.14

$ vi /etc/ssh/sshd_config
Match User access
ForceCommand internal-sftp
PasswordAuthentication yes
ChrootDirectory /var/sftp
PermitTunnel no
AllowAgentForwarding no
AllowTcpForwarding no
X11Forwarding no

$ systemctl restart sshd
```

# Next Notes

[[Process monitoring]]