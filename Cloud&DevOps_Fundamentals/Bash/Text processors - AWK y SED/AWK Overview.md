# Index

- [[#AWK OVERVIEW]]
- [[#Next Notes]]
# AWK OVERVIEW

The basic function of __awk__ is to search files for lines (or other units of text) that contain cartain patterns.

When a line matches one of the patterns, __awk__ performs specified actions on that line. __awk__ continues to process input lines in this way until it reaches the end of the input files.

__Awk__ breaks each line of input passed to it into fields. By default, a field is a string of consecutive characters delimited by whitespace (can be changed by -F). __Awk__ parses and operates on each separate field. This makes it ideal for handling structured text files -- especially tables -- data organized into consistent chunks, such as rows and columns.

When you run __awk__, you specify an awk program that tells __awk__ what to do. If no file is specified __awk__ will read from stdout.

```shell
$ awk [options] 'program' input-file1 input-file2 …
$ awk [options] -f program-file input-file1 input-file2 …
```

The program consist on a series of rules. Each rule specifies one pattern to search for and one action to perform upon finding the pattern.

```shell
$ # expression, i.e., $1 == "li".
$ # search pattern is a regular expression, i.e. /foo|bar|baz/.
$ # actions – statement(s) to be performed. $ $ # several patterns and actions are possible in awk.
$ # Single quotes around program is to avoid shell not to interpret any of its special characters.
$ # pattern { action }

$ awk '
    expression or /search pattern1/ { action }
    expression or /search pattern2/ { action }
    ' inut-file

$ # BEGIN rule is executed once only, before the first input record is read. 
$ # END rule is executed once only, after all the input is read.

$ awk '
     BEGIN { action }
       expression or /pattern/  { action }
     END   { action }
' input-file
```

# Next Notes

[[AWK Built-in Variables]]