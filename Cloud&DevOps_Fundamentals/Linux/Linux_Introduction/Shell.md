# Index

- [[#Shell]]
- [[#What is a shell]]
- [[#Basic Architecture of the Shell]]
- [[#Types]]
- [[#Comparison]]
- [[#Difference between Bash, Zsh and Other Linux Shells]]
- [[#Bourne Shell (sh)]]
- [[#C Shell (csh)]]
- [[#Newer shells]]
- [[#ash]]
- [[#dash]]
- [[#zsh]]
- [[#Next Notes]]

# Shell

## What is a shell

A shell is a program that provides an interface between a user and an operating system (OS) kernel.

## Basic Architecture of the Shell

![[shell.png]]

The fundamental architecture on which the hypothecal Shell is based isn't complex. The basic architecture is pretty similar to a pipeline, where input is analyzed and parsed, symbols are expanded. It uses a variety of methods such as brace, tilde, variable and parameter expansion and substitution, and filename generation. Then, commands are executed using shell built-in commands, or external commands.

## Types

- The Bourne Shell (sh)
- The C Shell (csh)
- The Korn Shell (ksh)
- The GBU Bourne-Again Shell (bash)

## Comparison

| Shell                             | Path                 | Default Promt (no-root user) | Default Prompt (root user) |
| --------------------------------- | -------------------- | ---------------------------- | -------------------------- |
| The Bourne Shell (sh)             | /bin/sh and /sbin/sh | $                            | #                          |
| The C Shell (csh)                 | /bin/csh             | %                            | #                          |
| The Korn Shell (ksh)              | /bin/ksh             | $                            | #                          |
| The GNU Bourne-Again Shell (bash) | /bin/bash            | bash-x.xx$                   | bash-x.xx#                 |
## Difference between Bash, Zsh and Other Linux Shells

### Bourne Shell (sh)

 The most prominent progenitor of modern shells is the Bourne Shell (sh) wich was named after it's creator Stephen Bourne. Released in 1979, it became the default command-interpreter in Unix because of its supports for command substitution, piping, variables, condition testing, and looping, along with other features. It did not offer much customization for users, and didn't support much modern niceties as aliases, command completion, and shell functions.
### C Shell (csh)

The C Shell (csh) was developed in the late 1970 by BillJoy at University of california, berkley. It added a lot of interactive elements with which users could control their systems, like aliases, job management abilities, command history, and more. It was modeled of the C Programming language, which the Unix operating system itself was written in.

## Newer shells

While the Linux community has settled on Bash in the years since, developers didn't stop creating new shells when Bash was first released 28 years ago.

### ash

Kenneth Almquist created a Bourne Shell clone known as Almquish shell, A Shell (ash), or sometimes just __sh__. It was also POSIX compatible and became the default shell in [BSD](https://www.howtogeek.com/190773/htg-explains-whats-the-difference-between-linux-and-bsd/) (Berkeley Software Distribution), a different branch of Unix. The __ash__ shel is more loghtweight than bash, which make it popular in embedded Linux systems.

### dash

Debian developed a shell environment based on ash and called it __dash__. It's designed to be POSIX-compliant and lightweight, so it's faster than Bash, but won't have all its features. Ubuntu uses the dash shell as it's default shell for non-interactive tasks, speeding up shell scripts and other tasks running in the background. Ubuntu still uses bash for interactive shells, however, so users still have the full-featured interactive environment.

### zsh

One of the most popular newer shell is __Z shell__ or __zsh__. Created by Paul Falstad in 1990, zsh is a Boune-style shell that contains the features you'll find in Bash, plus eben more. For example, zsh has spell-checking, the ability to watch for logins/logouts, some built-in programming features like bytecode, support for scientific notation in syntax , allows for flotating-point arithmetic, and more features.

# Next Notes

[[File systems]]