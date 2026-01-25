# Index

- [[#Sed script overview]]
- [[#Next Notes]]
# Sed script overview

A sed program consists of one or more sed commands, passed in by one or more of the __-e__, __-f__, __--expression__, and __--file__ options, or the first non-option argument if zero of these options are used.

Sed commands follow this syntax: \[addr]X\[options]:

- \[addr] is an optional line address. If \[addr] is specified, the command X will be executed only on the matched lines, \[addr] can be a single line number, a regular expression, or a range of lines.
- X is a single-letter sed command.
- Additional \[options] are used for some sed commands.

The following script deletes lines 30 to 35 in the input. 30, 35 is an address range. __d__ is the delete command:

```shell
$ sed '30,35d' input.txt > output.txt
```

The following script deletes any lines matching the regular expression __/\^foo/__. Address range here is __/\^foo/__.

```shell
$ sed '/^foo/d' input.txt > output.txt
```

Commands within a __script__ or __script-file__ can be separated by semicolons (;) or newlines.

The following example performs two sed operations: deleting any lines matching the regular expression __/\^foo/__, and replacing all occurrences of the string __hello__ with __w__ or __ld__:

```shell
$ sed '/^foo/d; s/hello/world/' input.txt > output.txt
```

> Commands a, c, i, due to their syntax, cannot be followed by semicolons working as command separators and thus should be terminated with newlines or be placed at the end of a script or script-file.

# Next Notes

[[Sed address overview]]