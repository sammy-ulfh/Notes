# Index

- [[#sed command overview]]
- [[#Next Notes]]
# sed command overview

![[Bash/Text processors - AWK y SED/images/001.png]]

Add the word hello after the second line:

```shell
$ seq 3 | sed '2a hello'
1
2
hello
3
```

Replace the 2nd to 9th lines with the word hello:

```shell
$ seq 10 | sed '2,9c hello'
1
hello
10
```

Deletes the second input line:

```shell
$ seq 3 | sed 2d
1
3
```

Insert the word hello before the second line:

```shell
$ seq 3 | sed '2i hello'
1
hello
2
3
```

Reads filename:

```shell
$ seq 3 | sed '2r/etc/hostname'
1
2
fencepost.gnu.org
3
```

Insert the word hello before the second line:

```shell
$ seq 3 | sed '2i hello'
1
hello
2
3
```

Transliterate a - j into 0 - 9

```shell
$ echo hello world | sed 'y/abcdefghij/0123456789/'
74llo worl3
```

The s command (as in substitute) is probably the most important in __sed__ nas has a lot of different options. The syntax of the s command is __s/regex/replacement/flags__

```shell
$ sed -i 's/erors/errors/g' input.txt
```

Its basic concept is simple: the s command attempts to match the pattern space against the supplied regular expression regexp; if the match is successful, then that portion of the pattern space which was matched is replaced with replacement.

The replacement can contain |n (n begin a number from 1 to 9, inclusive) references, which refer to the portion of the match which is contained between the nth anditsmatching. Also, the replacement can contain unescaped & characters which reference the whole matched portion of the pattern space.

Commonly used flags are:

- g - apply the replacement to all matches to the regexp, not just the first.
- i - the i modifies to regular-expression matching is a GNU extension which makes sed match regexp in a case-insensitive manner:

Replace bash login shell with false for all users:

```shell
$ sudo sed -i 's/bash/false/g' /etc/passwd
```

set bash login shell back only for vagrant user:

```shell
$ sudo sed -i '/vagrant/s/false/bash/g' /etc/passwd
```

# Next Notes

[[]]