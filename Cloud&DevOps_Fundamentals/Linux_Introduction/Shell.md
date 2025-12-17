# Index

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

 