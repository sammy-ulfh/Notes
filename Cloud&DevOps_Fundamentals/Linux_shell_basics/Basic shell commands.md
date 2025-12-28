# Index

- [[#Basic shell commands]]
  - [[#__Information__]]
  - [[#List of files]]
  - [[#PWD]]
  - [[#CD]]
  - [[#TOUCH]]
  - [[#MKDIR]]
  - [[#CP]]
  - [[#MV]]
  - [[#CAT CONCATENATION]]
  - [[#RMDIR & RM]]
- [[#Work with environment variables]]
- [[#View file content]]
- [[#Next Notes]]
# Basic shell commands

> Look carefully through the commands and try to find examples of their usage on practice manual.


__man__ - Main UNIX help. This is a command for working with system manual. Each page argument given to man is normally the name of a program, utility of function. A section, if provided, will direct man to look only in that section of the manual. 
The default action is to search in all of the available sections.

- __man cat__ - Get full guide for "cat" command
- __man man__ - Prints a list of options and description of man command
- __man -k__  - list prints a list of commands contains "list" in description
- __man -f ls__ - Get short description of "ls"

## __Information__

__info__ - information pages for commands, developed by GNU Project.

- __info cat__ - Get full guide for cat command.
- __info info__ - Prints a full description of info command

## List of files

__ls__ - view information about files or directories (list)

- __ls -la__ - List files, use a long listing format, do not ignore entries starting with.
- __ls -lh__ - List files, use a long list format, print human readable sizes (1K, 234M, 2G)
- __ls -lt__ - List files, use a long list format, sort by modification time, newest first.
- __ls -lSh__ - List files, use a long list format, sort by file size (largest first), print human readable size.

## PWD

__pwd__ - print working directory - shows full path for working directory

```shell
pwd
/home/user
```

## CD

__cd__ - change current directory

Environment variable $HOME is the default dir. The variable $CDPATH defines the search path for the directory containing dir. Alternative directory names in $CDPATH are separated by a colon (;). A null directory name in $CDPATH is the same as the current directory (.). If dir begins with a slash, then $CDPATH is not used.

__cd /__ - change the current directory to __/__ - roof folder of a filesystem
__cd ..__ - change current directory the parent of the previous one directory
__cd ~__ - change current directory to user's home dir
__cd -__ - change current directory to the previous one

```
$ pwd

/home/vagrant  
  

$ cd /tmp

$ pwd
/tmp

  
$ cd -  

/home/vagrant

$ pwd  
/home/vagrant   
$ cd -   
/tmp   
$ pwd  
/tmp
```

## TOUCH

__touch__ - create an empty file / change time label for given file with parameter:

-d, --date=STRING

parse string and use it instead of current time. STRING is a mostly free format readable date string such as "Sun,29 Feb 2004 16:21:42 -0800" or "2004-02-29 16:21:42" or even "next Thursday"

```
$ touch newfile.txt
$ ls -l newfile.txt
-rw-rw-r-- 1 vagrant vagrant 0 Aug 23 16:16 newfile.txt
$ touch -d "next Friday" newfile.txt
$ ls -l newfile.txt
-rw-rw-r-- 1 vagrant vagrant 0 Aug 30 2019 newfile.txt
```

## MKDIR

__mkdir__ - make directory - create an empty directory

-m, --mode=MODE

set file mode (as in chmode), not a rwx - umask

-p, --parents

no error if existing, make parent directories as needed.

```
$ mkdir empty
$ ls -l
total 0
drwxrwxr-x 2 vagrant vagrant  6 Aug 23 16:26 empty

$ mkdir -p dir/test{1..3}/empty
$ tree
.
└── dir
    ├── test1
    │   └── empty
    ├── test2
    │   └── empty
    └── test3
        └── empty
```

## CP

__cp__ - copy file / directory with all subdirectories

-p same as --preserve=mode,ownership,timestamps
--preserve\[ATTR_LIST]

preserve the special attributes (default: mode, ownership, timestamps), if possible additional attributes: context, links, xattr, all

-R, -r, --recursive

copy directories recursively

-i, --interactive

prompt before overwrite (overrides a previous -n option)

```
$ cp -r dir dir2/
$ tree dir2/
dir2/
└── dir
    ├── test1
    │   └── empty
    ├── test2
    │   └── empty
    └── test3
        └── empty
```

## MV

__mv__ - move or rename file / directory

-i, --interactive

prompt before overwrite

--backup\[=CONTROL]

make a backup of each existing destination file, like --backup but does not accept an argument.

-S, --suffix= SUFFIX

override the usual backup suffix.

-u, --update

move only when the source file is newer than the destination file or when the destination file is missing

```
$ tree
.
├── dir
│   └── newfile
└── newfile

$ mv -b -S ".old" newfile dir/
$ tree 
.
└── dir
    ├── newfile
    └── newfile.old
```

## CAT CONCATENATION

__cat__ - concatenation - display content of file or combine file into a single file

```
$ echo 1 > 1.txt
$ echo 2 > 2.txt
$ cat 1.txt 2.txt > 3.txt
$ cat 3.txt 
1
2
```

## RMDIR & RM

__rmdir__ - remove directory - remove __empty__ directory
__rm__ - remove file or directory, remove (unlink) the FILE(s).

> If you use rm to remove a file, it might be possible to recover some of its content, given sufficient expertise and/or time. For greater assurance that the contents are truly unrecoverable, consider using __shred__.


-f, --force

Ignore non existing files and arguments, never prompt

-r, -R, --recursive

remove directories and their contents recursively

```
$ rm -v ~/1.txt 
removed '/home/vagrant/1.txt'
$ rm -rfv dir/
removed 'dir/newfile.old'
removed 'dir/newfile'
removed directory: 'dir
```

# Work with environment variables

There are several commands available that allow you to list and set environment variables in Linux:

- __env__ - The command allows to run another program in a custom environment without modifying the current one.
  > When used without an argument it will print a list of current environment variables.
- __printenv__ - The command __print all__ or __the specified__ environment variables.
- __set__ - The command sets or unsets shell variables.
  > When used without an argument it will print a __list of all variables__ including __environment and shell variables, and shell functions__
- __unset__ - The command deletes shell and environment variables.
- __export__ - The command sets environment variables.

[Examples](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/)

# View file content

__more__ is an old utility. When the text passed to it is too large to fit on one screen, it pages it. You can scroll down but not up.

__less__ was written by a man who was fed up with more's inability to scroll backwards through a file. He turned less into an open source project and over time, various individuals added new features to it. less is massive now. That;s why some small embedded systems have more but not less.

/pattern

__Search forward__ in the file for the N-th line containing the pattern. The search starts at the line immediately before the top line displayed.

n - Repeat dprevious search, for N-th line containing the last pattern.
N - Repeat previous search, but in the reverse direction.

__head__ - output the first 10 lines of a file.

-n, --lines=\[-]K

Print the first K lines, instead of the last 10; or use -n +K to output starting with the Kth

-f, --follow\[={name|descriptor}]

output appended data as the file grows.

# Next Notes

[[Text editors]]

