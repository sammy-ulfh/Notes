# Index

- [[#AWK Examples]]
	- [[#Default behavior]]
	- [[#Print the lines which match the given pattern]]
	- [[#Splitting a line into fields]]
	- [[#Use of NR built-in variables (display line number)]]
	- [[#Use of NF built-in variables (display last field)]]
- [[#Next Notes]]
# AWK Examples

## Default behavior

By default Awk prints every line of data from the specified file.

```shell
$ awk '{print}' employee.txt

ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000
```

## Print the lines which match the given pattern

The awk command prints all the line which matches with the 'manager'.

```shell
$ awk '/manager/ {print}' employee.txt 

ajay manager account 45000
varun manager sales 50000
amit manager account 47000
```

## Splitting a line into fields

For each record i.e line, the awk command splits the record delimited by whitespace character by default and stores it in the $n variables. If the line has 4 words, it will be stored in $1, \$2, \$3 and \$4 respectively. Also, \$0 represents the whole line.

```shell
$ awk '{print $1,$4}' employee.txt

ajay 45000
sunil 25000
varun 50000
amit 47000
tarun 15000
deepak 23000
sunil 13000
satvik 80000
```

## Use of NR built-in variables  (display line number)

The awk command with __NR__ prints all the lines along with the line number.

```shell
$ awk '{print NR,$0}' employee.txt 

1 ajay manager account 45000
2 sunil clerk account 25000
3 varun manager sales 50000
4 amit manager account 47000
5 tarun peon sales 15000
6 deepak clerk sales 23000
7 sunil peon sales 13000
8 satvik director purchase 80000
```

## Use of NF built-in variables  (display last field)

__\$1__ represents Name and __\$NF__ represents Salary. We can get the Salary using __\$NF__, where __\$NF__ represents last field.

```shell
$ awk '{print $1,$NF}' employee.txt

ajay 45000
sunil 25000
varun 50000
amit 47000
tarun 15000
deepak 23000
sunil 13000
satvik 80000
```

# Next Notes

[[Sed overview]]