# Index

- [[#Variables]]
	- [[#Assigment]]
	- [[#Referencing a variable]]
	- [[#Indirect referencing]]
	- [[#Variable types]]
	- [[#Manipulating strings]]
	- [[#Parameter substitution]]
	- [[#Special variable types]]
	- [[#Local variables]]
	- [[#Environment variables]]
	- [[#Positional parameters]]
	- [[#Built-in variables]]
	- [[#Special shell variables]]
	- [[#Arrays]]
- [[#Next Notes]]
# Variables

Variables are how programming and scripting languages represent data. A variable is nothing more than a label, a name assigned to a location or set of locations in computer memory holding an item of data.

## Assigment

```shell
var=value
vas2="one two three"
var3=one\ two\ three
```

## Referencing a variable

```shell
echo $var
echo ${var}
```

## Indirect referencing

```shell
var=value
value=hello
eval b=\$$var

echo $b
```

## Variable types

Bash does not segregate its variables by "type".

Essentially, Bash variables are character strings, but, depending on context, Bash permits arithmetic operations and comparisons on variables. The determining factor is whether the value of a variable contains only digits.

The declare or typeset built-ins, which are exact synonyms, permit modifying the properties of variables.

```shell
$ n=6/3
$ echo "n = $n"
n = 6/3

$ declare -i n
$ n=6/3
$ echo "n = $n"
n = 2
```

## Manipulating strings

Bash supports a surprising number of strings manipulation operations.

- __${#var}__ - $var length. For an array, ${#array} is the length of the first element in the array.

```shell
$ stringZ=abcABC123ABCabc
$ echo ${#stringZ}
15

$ arrayX=(a ab abc)
$ echo ${#arrayX}
1
```

- __${var:position:length}__ - extracts $length characters of substring from $var at $position. 0-based indexing.

```shell
$ stringZ=abcABC123ABCabc
$ echo ${stringZ:2:5}
cABC1
```

- __${var#Pattern}__ - Remove from $var the __shortest__ part of $pattern that matches the __front__ end of $var.
- __${var##Pattern}__ - Remove from $var the __longest__ part of $pattern that matches the __front__ end of $var.

```shell
$ stringZ=abcABC123ABCabc
$ echo ${stringZ#a*C}
123ABCabc
$ echo ${stringZ##a*C}
abc
```

- __${var%Pattern}__ - deletes shortest match of $Pattern from __back__ of $var.
- __${var\%%Pattern}__  - deletes longest  match of $Pattern from __back__ of string.

```shell
$ stringZ=abcABC123ABCabc
$ echo ${stringZ%a*c}
abcABC123ABC
$ echo ${stringZ%%b*c}
a
```

- __${var/Pattern/Replacement}__ - replace __first__ match of $Pattern with $Replacement. If $Replacement is omitted, then the first match of $Pattern is replaced by nothing, that is, __deleted__.
- __${var//Pattern/Replacement}__ - replace all matches of $Pattern with $Replacement.

```shell
$ stringZ=abcABC123ABCabc
$ echo ${stringZ/abc/xyz}
xyzABC123ABCabc
$ echo ${stringZ//abc/xyz}
xyzABC123ABCxyz
$ stringZ=abcABC123ABCabc
$ echo ${stringZ/abc}
ABC123ABCabc
$ echo ${stringZ//abc}
ABC123ABC
```

- __${var/#Pattern/Replacement}__ - If __prefix__ of $var matches $Pattern, then substitute $Replacement for $Pattern
- __${var/%Pattern/Replacement}__ - If __suffix__ of $var matches $Pattern, then substitute $Replacement for $Pattern

```shell
$ stringZ=abcABC123ABCabc
$ echo ${stringZ/#abc/XYZ}
XYZABC123ABCabc
$ echo ${stringZ/%abc/XYZ}
abcABC123ABCXYZ
```

## Parameter substitution

- __${parameter-default}__, __\${parameter:-default}__ - If $parameter not set, use default. __\${parameter-default}__ and __\${parameter:-default}__ are almost equivalent. The extra ":" makes the difference only when $parameter has been declared, but is null.

```shell
$ var1=1
$ var2=2
$ echo ${var1-$var2}
1
$ echo ${var3-$var2}
2
$ var1=1
$ var3=           # declared but null
$ echo ${var3-$var1}
$ echo ${var3:-$var1}
1
```

The default parameter construct finds use in providing "missing" command-line arguments in scripts.

```shell
#!/bin/bash

DEFAULT_FILENAME=generic.data

# If not otherwise specified, the following command block operates on the
# file "generic.data".

filename=${1:-$DEFAULT_FILENAME}
...
```

- __${parameter=default}, __\${parameter:=default}__ - If $parameter not set, set it to $default. Both forms nearly equivalent. The ":" makes the difference only when $parameter has been declared and is null.

```shell
$ varZ= 
$ echo ${varZ=abc}
$ echo ${varZ:=abc}
abc
$ echo ${var=abc}
abc
$ echo ${var=xyz}
abc
```

- __${parameter+alt_value}__, and __\${parameter:+alt_value}__ allow you to substitute an alternative value if a variable is set:
  
  - __${parameter+alt_value}__ returns alt_value if the variable is set, even if it is empty.
  - __${parameter:+alt_value}__ - returns alt_value only if the variable is set and not empty.

```shell
# Example with undefined parameter for **${parameter+alt_value}**  

$ a=${param_undefined+xyz}  
$ echo "a = $a"   
a = # because param_undefined is not defined at all

  
# Example with empty parameter for **${parameter+alt_value}**  

$ param1=

$ a=${param1+xyz}  
$ echo "a = $a"   
a = xyz # because param1 is set, even if empty  
  

# Example with empty parameter for **${parameter:+alt_value}**

$ param2=   
$ a=${param2:+xyz}   
$ echo "a = $a"   
a = # because param2 is set, but empty  
  

# Example with parameter with value for **${parameter:+alt_value}**  
$ param3=123  
$ a=${param3:+xyz}  

$ echo "a = $a"  

a = xyz # because param3 is set and not empty
```

- __${parameter?err_msg}__, __\${parameter:?err_msg}__ if $parameter set, use it, else print $err_msg and abort the script with an exit status of 1. Both forms nearly equivalent. The ":" makes a difference only when parameter has been declared and is null.
```shell
#!/bin/bash

: ${HOSTNAME?} ${USER?} ${MAIL?}
echo "Name of the machine is $HOSTNAME."
echo "You are $USER."
echo "Your mail INBOX is located in $MAIL."
echo
echo "If you are reading this message,"
echo "critical environmental variables have been set."
echo
```

## Special variable types

- Local variables
- Environment variables
- Positional parameters
- Built-int variables

## Local variables

Variables visible only within a code block or function.

```shell
$ func() {
  local var=$1
  echo $var
}

$ echo $var
$ func Hello
Hello
```

## Environment variables

Variables that affect the behavior of the shell and user interface.
Environment variables can be set:

- system-wide:
  - /etc/environment
- For current session:
  - export MY_VAR=valur
- For all session of a user:
  - ~/.bashrc
  - ~/.bash_profile
- During script execution:

```shell
#!/bin/bash

. ~/my_env_vars # or: source ~/my_env_vars
```

How to check current environment variables?

```shell
$ env
LC_ADDRESS=en_US.UTF-8
HOSTNAME=node1
LC_MONETARY=en_US.UTF-8
TERM=xterm-256color
SHELL=/bin/bash
HISTSIZE=1000
SSH_CLIENT=10.0.2.2 37896 22
LC_NUMERIC=en_US.UTF-8
SSH_TTY=/dev/pts/0
USER=vagrant
...
```

## Positional parameters

Arguments passed to the script from the command line: $0, $1, $2, $3. . .

__$0__ is the name of the script itself, __\$1__ is the first argument, __\$2__ the second, __\$3__ the third, and so forth.

After __\$9__, the arguments must be enclosed in brackets, fir example, __\${10}__, __\${11}__, __\${12}__.
__$#__ number of command-line arguments or positional parameters.

The special variables "__$\*__" and __\$@__ denote all the positional parameters.

```shell
#!/bin/bash

NUMBER=1

for arg in $@; do
  echo -e "argument #${NUMBER}: $arg";
  ((NUMBER++));
done
```
> $ bash script.sh 1 apple hello 4
argument #1: 1
argument #2: apple
argument #3: hello
argument #4: 4

## Built-in variables

![[004.png]]

## Special shell variables

![[005.png]]

## Arrays

An array is a variable containing multiple values. Any variable may be used as an array. There is no maximum limit to the size of an array, nor any requirement that member variables be indexed or assigned contiguously.

Arrays are __zero-based__: the first element is indexed with the number 0.

```shell
$ my_array=( zero one two three four five
```

Array elements may be initialized with the following notation:

```shell
$ my_array[6]=six
```

Alternatively, a script may introduce the entire array by an explicit statement:

```shell
declare -a new_array
```

To dereference (retrieve the contents of) an array element, use curly bracket notation:

```shell
$ echo ${my_array[6]}
six
```

Refer all array elements:

```shell
$ my_array=( zero one two three four five )
$ echo ${my_array[@]}
zero one two three four five six
$ echo ${my_array[*]}
zero one two three four five six
```

Get the number of the elements in array:

```shell
$ echo ${#my_array[@]}
7
$ echo ${#my_array[*]}
7
```

# Next Notes

[[Conditions]]


