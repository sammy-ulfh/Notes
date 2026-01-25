# Index

- [[#Sed overview]]
	- [[#SED]]
	- [[#SED options]]
- [[#Next Notes]]
# Sed overview

## SED

A stream __ED__ itor is used to perform basic transformations on text read from a file or a pipe. The result is sent to __standard output__. The syntax for the sed command has no output file specification, but results can be saved to a file using output redirection. The editor does not modify the original input. The sed tool is often used to perform find-and-replace action on lines containing pattern.

```shell
$ sed OPTIONS... [SCRIPT] [INPUTFILE...]
```

For example, to replace all occurrences of __hello__ to __w__ or __ld__ in the file input.txt:

```shell
$ sed 's/hello/world/' input.txt > output.txt
```

If you do not specify __INPUTFILE__, or if __INPUTFILE__ is -, sed filters the contents of the standard input. The following commands are equivalent:

```shell
$ sed 's/hello/world/' input.txt > output.txt
$ sed 's/hello/world/' < input.txt > output.txt
$ cat input.txt | sed 's/hello/world/' - > output.txt
```

## SED options

- __-n__
- __--quiet__
- __--silent__

By default, sed prints out the pattern space at the end of each cycle through the script. These options disable this automatic printing, and sed only produces output when explicitly told to via the __p__ command.

# Next Notes

[[Sed script overview]]