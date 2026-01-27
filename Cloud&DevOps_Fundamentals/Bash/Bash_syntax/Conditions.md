# Index

- [[#Conditions]]
	- [[#Test command]]
	- [[#Test command expressions]]
	- [[#Extended test commands]]
	- [[#Double parentheses]]
	- [[#IF/THEN]]
	- [[#CASE]]
	- [[#List construct]]
- [[#Next Notes]]
# Conditions

In terms of conditions bash has:

- __test__ command or square brackets __\[ ]__
- extended testcommand __\[\[ ]]__
- double parentheses  __(( ))__ and __let__ command
- __if/then__ construct
- __case__ statements
- list constructs

## Test command

__\[__ (__left bracket__ special character) is a synonym for  __test__, and built-in for efficiency reasons.

This command consider its arguments as comparison expressions or file test and __returns an exit status corresponding to the result of the comparison__ (0 for true, 1 for false).

__test__ EXPRESSION

\[ EXPRESSION ]

```shell
$ ls
file.txt

$ test -f file.txt && echo "File exists"
File exists

$ [ -f file.txt ] && echo Indeed
Indeed

$ [ -f file1.txt ] || echo No such file
No such file
```

Checking exist status of a command in a script:

```shell
#!/bin/bash

...
ifup eth0
[ $? -ne 0 ] && rc=1
```

## Test command expressions

![[006.png]]

## Extended test commands

With version 2.02, Bash introduced the \[\[ ... ]] extended test command, which performs comparisons in a manner more familiar to programmers from other languages. Note that \[\[ is a keyword, not command.

Bash sees \[\[ $a -lt $b ]] as a single element, which returns an exit status. Using the \[\[ ... ]] test construct, rather than __\[ ... ]__ can prevent many logic errors in scripts. For example, the &&, | |, <, and > operators work within a \[\[ ]] test, despite giving an error within a \[ ] construct.

```shell
$ string_with_spaces='some spaces here'
$ if [[ -n $string_with_spaces ]]; then
    echo "The string is non-empty";
  fi

The string is non-empty
```

```shell
$ if [ -n $string_with_spaces ]; then
> echo "The string is non-empty";
> fi

-bash: [: too many arguments
```

## Double parentheses

The __(( ... ))__ and __let ...__ constructs return an exit status, according to whether the arithmetic expressions they evaluate expand to an non-zero value.

If the value of the expression is non-zero, the return status is 0; otherwise the return status is 1.

These arithmetic-expansion constructs may therefore be used to perform arithmetic comparison.

```shell
$ (( 0 && 1 ))
$ echo $?
1

$ var=-2 && (( var+=2 ))
$ echo $?
1
```

For arithmetic expressions see __man bash__ "ARITHMETIC EVALUATION" section.

## IF/THEN

An __if/then__ construct test whether the exit status of a list of commands is 0 (since 0 means "success" by UNIX convention), and if so, executes one or more commands.

An __if__ can test any command, not just conditions enclosed within brackets.

Syntax:

```shell
if [ condition1 ]; then
  command1
  command2
elif [ condition2 ]; then
  command4
  command5
else
  default-command
fi
```

Example (__/etc/init.d/network__):

```shell
...
rootfs=$(awk '{ if ($1 !~ /^[ \t]*#/ && $2 == "/" && $3 != "rootfs") { print $3; }}' /proc/mounts)
if [[ "$rootfs" == nfs* || "$rootopts" =~ _r?netdev ]] ; then
        exit 1
fi
...
if [ ! -d /proc/net/vlan ] && ! modprobe 8021q >/dev/null 2>&1 ; then
        net_log $"No 802.1Q VLAN support available in kernel."
fi
...
```

## CASE

```shell
case EXPRESSION in
  case1)
    command1;
    command2;
  ;;
  case2)
    command3
  ;;
  …
  caseN)
    commandM
  ;;
esac
```

Each case is an expression matching pattern. Each clause must be terminated with ";;". Each case statement is ended with the __esac__ statement.

Init script example:

```shell
case "$1" in
        start)
            start
            ;;

        stop)
            stop
            ;;
        condrestart)
            if test "x`pidof anacron`" != x; then
                stop
                start
            fi
            ;;
        *)
            echo $"Usage: $0 {start|stop|restart|condrestart|status}"
            exit 1
esac
```

Bash script with arguments example:

```shell
#!/bin/bash

set -euo pipefail

MESSAGE=""
COUNT=5

help() {
  echo -e "\nUsage: $0 [OPTION]";
  echo "";
  echo -e "\t-m\tmessage to print"
  echo -e "\t-n\tnumber of messages to print. Default 5"
  echo -e "\t-h\tget help"
}

[[ -z "$@" ]] && help && exit 1;

for arg in "$@"; do
  case $arg in
    -m) MESSAGE=$2;
      shift;
      shift;
      ;;
    -n) COUNT=$2;
      shift;
      shift;
      ;;
    -h) help; exit 0;
      ;;
  esac
done

for i in $(seq 1 $COUNT); do
  echo $MESSAGE;
done
```

```shell
$ ./args.sh 
Usage: ./args.sh [OPTION]
    -m    message to print
    -n    number of messages to print. Default 5
    -h    get help

$ ./args.sh -m Hello
Hello
Hello
Hello
Hello
Hello

$ ./args.sh -m Hi -n 1
Hi
```

## List construct

The "__and list__" and "__or list__" constructs provide a means of processing a number of commands consecutively.

These can effectively replace complex nested if/then of even case statements.

__AND list__

Each command executes in turn, provided that the previous command has given a return value of __true__ (zero). At the first false (non-zero) return, the command chain terminates (the first command returning false is the last one to execute).

```shell
$ command-1 && command-2 && command-3 && ... command-n
```

__OR list__

Each command executes in turn for as long as the previous command returns __false__. At the first return, the command chain terminates (the first command returning true is the lst one to execute).

```shell
$ command-1 || command-2 || command-3 || ... command-n
```

# Next Notes

[[Bash/Bash_syntax/Loops]]