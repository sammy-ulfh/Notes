# Index

- [[#SED address overview]]
- [[#Next Notes]]
# SED address overview

Addresses determine on which line(s) the sed command will be executed.

The following command replaces the word hello with world only on line 144:

```shell
$ sed '144s/hello/world/' input.txt > output.txt
```

If no addresses are given, the command is performed on all lines.

The following command replaces the word __hello__ with __world__ on all lines in the input file:

```shell
$ sed 's/hello/world/' input.txt > output.txt
```

Addresses can contain regular expressions to match lines based on content instead of line numbers. The following command replaces the word 'hello' with 'world' only in lines containing the word 'apple':

```shell
$ sed '/apple/s/hello/world/' input.txt > output.txt
```

__/regexp/__

This will select any line which matches the regular expression regexp. If regexp itself includes any /characters, each must be escaped by backslash (\\).

__\\%regexp%__

(The % may be replaced by any other single character.)

This also matches the regular expression regexp, but allows one to use a different delimiter than /. This is particularly useful if the regexp itself contains a lot of slashes, since it avoids the tedious escaping of every /. If regexp itself includes any delimiter characters, each must be escaped by a backslash (/).

```shell
$ sed -n '/^\/home\/alice\/documents\//p'
$ sed -n '\%^/home/alice/documents/%p'
$ sed -n '\;^/home/alice/documents/;p'
```

Appending the __!__ character to the end of an address specification (before the command letter) negates the sense of the match. That is, if the ! character follows an address or an address range, then only lines which __do not match__ the addresses will be selected.

The following command replaces the word __hello__ with __world__ only in lines __not___ containing the word __apple__:

```shell
$ sed '/apple/!s/hello/world/' input.txt > output.txt
```

# Next Notes

[[Sed command overview]]