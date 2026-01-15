# Index

- [[#Bash options]]
	- [[#Example 1]]
	- [[#Example 2]]
- [[#Next Notes]]

# Bash options

Options are settings that change shell and/or script behavior.

The __set__ command enables options within a script. At the point in the script where you want the options __to take effect__, use __set -o option-name__ or, in short form, __set -option-abbrev__. These two forms are equivalent:

- __set -o verbose__
- __set -v__

To __disable__ an option within a script, use set __+o option_name___ or __set -option-abbrev__.

- __set +o verbose__
- __set +v__

![[001.png]]

## Example 1

```shell
#!/bin/bash

# exit_on_error.sh
set -e

echo "Check non-existing file"
cat non-existing-file.txt 
echo "moving on"
```
>$ ./exit_on_error.sh
> 	Check non-existing file
> 	cat: non-existing-file.txt: No such file or directory

## Example 2

```shell
#!/bin/bash

# skip_error.sh
# default value is +e

echo "Check non-existing file"
cat non-existing-file.txt 
echo "moving on"
```
>$ ./skip_error.sh 
Check non-existing file
cat: non-existing-file.txt: No such file or directory
moving on

# Next Notes

[[Exit Codes]]