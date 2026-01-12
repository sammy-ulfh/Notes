# Index

- [[#Introduction to shells]]
	- [[#What is shell?]]
	- [[#Shell types]]
	- [[#Shell auto-completion]]
	- [[#Bash startup files]]
- [[#Next notes]]
# Introduction to shells
## What is shell?

- The UNIX Shell program interprets user commands, which are either directly entered by the user, or which can be read from a file called the shell script or shell program.

- Shell scripts are interpreted, not compiled.
- The shell reads commands from the script line per line and searches for those commands on the system, while a compiler converts a program into machine readable form, an executable file -which may then be used in a shell script.
- Apart from passing commands to the kernel, the main task of a shell is providing a user environment, which can be configured individually using shell resource configuration files.
- The file __/etc/shells__ gives an overview of known shell on a Linux system.
- To switch from one shell to another, just enter the name of the new shell in the active terminal.

>`sh`
>`bash`
>`zsh`

![[change_shell.png]]

## Shell types

- __sh__ or __Bourne Shell__: the original shell still used on UNIX systems and in UNIX-related environments. This is the basic shell, a small program with few features. While this is not the standard shell, it is still available on every Linux system for compatibility with UNIX programs.
- __bash__ or __Bourne Again Shell__: the standard GNU shell, intuitive and flexible. Probably most advisable for beginning users while being at the same time a powerful tool for the advanced and professional user. On Linux, bash is the standard shell for common users. This shell is a so-called superset of the Bourne Shell, a set of add-ons, and plugins. This means that the Bourne Again Shell is compatible with the Bourne Shell: commands that work in sh, also work in bash. However, the reverse is not always the case.
- __csh__ or __C shell__: the syntax of this shell resembles that of the C programming language. Sometimes asked for by programmers.
- __tcsh__ or __TENEX C shell__: a superset of the common C shell, enhancing user-friendliness and speed. That is why some also call it the Turbo C shell.
- __ksh__ or __the Korn shell__: sometimes appreciated by people with a UNIX background. A superset of the Bourne Shell; with standard configuration a nightmare for beginning users.

## Shell auto-completion 

Some shell like bash or zsh support auto-completion of entered commands or paths. For example, if you being typing __cd /ro__ and then pressing on __Tab__ key on a keyboard and entered path in command line is completed to full __cd /root/__.

```shell
cd /ro # now you press Tab here and get
cd /root/
```

If you press __Tab__ one more time, shell will give you a hint with a list of files and directories inside __/root/__ folder.

```shell
cd /root/ # now you press Tab here an get
cd /root/. # . - dot character was added because all file/dir name starts with it

./ ../ .bashrc .docker/ .profile

cd /root/.b # if you type .b and press Tab again, you will get
cd /root/.bashrc
```

Auto-completion in Linux is also configurable, you can see more details in [this link](https://faun.pub/configure-bash-auto-completion-tab-completion-on-linux-db0d9310818b).

## Bash startup files

Startup files are scripts that are read and executed by Bash when it starts. The following subsections describe different ways to start the shell, and the startup files that are read consequently.

__Invoked as an interactive login shell, or with --login__

Interactive means you can enter commands. The shell is not running because a script has been activated. A login shell means that you got the shell after authenticating to the system, usually by giving your user name and password.

Files read:

- /etc/profile
- ~/.bash_profile
- ~/.bash_login or ~/.profile: first existing readable file is read
- ~/.bash_logout upon logout

__Invoked as interactive non-login shell__

A non-login shell means that you did not have to authenticate to the system. For instance, when you open a terminal using an icon, or a menu item, that is a non-login shell.

Files read:

- ~/.bashrc

This file is usually referred to in ~/.bash_profile

# Next notes

[[Linux/Linux_shell_basics/Shell programming]]