# Index

- [[#Script Development and Invocation]]
- [[#Next Notes]]

# Script Development and Invocation

In the simplest case, a script is nothing more than a list of system commands stored in a file. At the very least, this saves the effort of retyping that particular sequence of commands each time it is invoked.

The __sha-bang (#!)__ at the head of a script tells your system that this file is a set of commands to be fed to the command interpreter indicated. Immediately following the __sha-bang__ is a path name. This is the path to the program that interprets the commands in the script, whether it be a shell, a programming language or a utility.

- __#!/bin/sh__
- __#!/bin/bash__
- __#!/usr/bin/perl__
- __#!/usr/bin/env python__
- __#!/bin/sed -f__
- __#!/bin/awk -f__

Having written the script, you can involve it by __sh__ scriptname, or alternatively bash scriptname.

Much more convenient is to make the script itself directly executable with a chmod and run it by __./scriptname__

# Next Notes

[[Bash options]]