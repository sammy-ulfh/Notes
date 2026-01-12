# Index

- [[#Bash startup files]]
  - [[#__Invoked as an interactive login shell or with '--login'__]]
  - [[#__Invoked as an interactive non-login shell__]]
- [[#Next Notes]]

# Bash startup files

Startups files are scripts that are read and executed by bash when it starts. The following subsections describe different ways to start the shell, and the startup files are read consequently.

## __Invoked as an interactive login shell or with '--login'__

Interactive means you can enter commands. The shell is not running because a script has been activated. 

A login shell means that you got the shell after authenticating to the system, usually by giving your user name and password.

File read:
<
- __/etc/profile__
- __~/.bash_profile, ~/.bash_login or ~/.profile__ (first existing readable file is read)
- __~/.bash_logout__ (upon logout)

## __Invoked as an interactive non-login shell__

A non-login shell means that you did not have to authenticate to the system. For instance, when you open a terminal using an icon, or a menu item, that is non-login shell.

Files read:

- __~/.bashrc__

This file is usually referred to in __~/.bash_profile__.

# Next Notes

[[Bash/Bash_Introduction/Shell programming]]

