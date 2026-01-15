# Index

- [[#Loops]]
	- [[#For loop]]
	- [[#While loop]]
	- [[#Until loop]]
	- [[#Loop control]]
- [[#Next Notes]]

# Loops

A loop is a block of code that iterates a list of commands as long as the __loop control condition is true__.

- For
- While
- Until

## For loop

During each pass through the loop, __arg__ takes one value of each successive variable in the list.

```shell
for arg in [list]; do
    command(s)...
done
```

Example:

```shell
for file in "$( find . -type l )"; do
    echo "$file"
done | sort
```

## While loop

This construct test for a condition at the top of the loop, and keeps looping as long as that condition is true (returns a 0 exit status). In contrast to a for loop, a while loop finds use in situations where the number of loop repetitions is not known beforehand.

```shell
while [ condition ]; do
  command(s)...
done
```

Example:

```shell
LIMIT=10

while [ "$a" -le $LIMIT ] ; do
  echo -n "$a "
  let "a+=1"
done
```

## Until loop

This construct test for a condition at the top of a loop, and keeps looping as long as that condition is false (opposite of while loop).

```shell
until [ condition-is-true ] ; do
    command(s)…
done
```

## Loop control

+ __break__: the break command terminates the loop (breaks out of it).
+ __continue__: the continue command causes a jump to the next iteration of the loop, skipping all the remaining commands in that particular loop cycle.

```shell
$ for i in {1..5}; do
    echo $i
    [[ $i -eq 3 ]] && break
  done
1
2
3
```

# Next Notes

[[I-O Recirection]]