# Index

- [[#Functions]]
	- [[#Exit status]]
	- [[#return]]
- [[#Next Notes]]
# Functions

A function is a subroutine, a code block that implements a set of operations , a "black box" that performs a specified task . Wherever there is a repetitive code, when a task repeats with only slight variations in procedure, then consider using a function.

```shell
function_name () {
  command...
}
```

Functions may process arguments passed to them an return an exit status to the script for further processing.

```shell
$ function_name $arg1 $arg2
```

The function refers to the passed arguments by position (as if they were positional parameters), that is, $1, $2, and so forth.

```shell
$ print_args () {
  local var1=$1
  local var2=$2
  echo "first function argument is:" $var1
  echo "second function argument is:" $var2
}

$ print_args /tmp hello
first function argument is: /tmp
second function argument is: hello 
```

## Exit status

Functions return a value, called an exit status. This is analogous to the exit status returned by a command. The exit status may be explicitly specified by a return statement, otherwise it is the exit status of the last command in the function (0 is successful, and non-zero error code if not). This exit status may be used in the script by referencing it as $?.

## return

Terminates a function. A return command optionally takes an integer argument, which is returned to the calling script as the "exit status" of the function, and this exit status assigned to the variable $?.

```shell
#!/bin/bash

retfunc() {
  echo "this is retfunc()"
  return 1
}

exitfunc() {
  echo "this is exitfunc()"
  exit 1
}

retfunc
echo "We are still here"

exitfunc
echo "We will never see this"
```
> $ ./func.sh
this is retfunc()
We are still here
this is exitfunc()

# Next Notes

[[Environment]]