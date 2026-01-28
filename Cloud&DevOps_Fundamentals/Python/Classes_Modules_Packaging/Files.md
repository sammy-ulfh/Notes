# Index

- [[#Files]]
	- [[#open]]
	- [[#File attributes]]
	- [[#write()]]
	- [[#read()]]
	- [[#File handling]]
	- [[#Directory]]
- [[#Next Notes]]
# Files

## open

file object = open(file_name \[, access_mode]\[, buffering])

## File attributes

![[file_attributes.png]]

```python
# Open a file
with open("foo.txt", "w") as fo:
    print("Name of the file: ", fo.name)
    print("Closed or not : ", fo.closed)
    print("Opening mode : ", fo.mode)  
  
------  
Output:  
Name of the file:  foo.txt
Closed or not :  False
Opening mode :  w
```

## write()

"a" - append output to the end of file or create a new one if it doesn't exist

```python
with open("foo.txt", "a") as fo:
    fo.write( "Python is a great language.\nYeah, it's great!!\n")
```

"w" - rewrite the file with the new content or create a new one  if it doesn't exist

```python
with open("foo.txt", "w") as fo:
    fo.write( "Python is a great language.\nYeah, it's great!!\n")
```

## read()

foo.txt:

```txt
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
```

Read 10-characters from file:

```python
with open("foo.txt") as fo:
    s = fo.read(10)
    print(s)

------
Output:  
Explicit i
```

Read the whole file:

```python
Read the whole file:

with open("foo.txt") as fo:
    s = fo.read()
    print(s)

------
Output:  
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
```

Read the file line by line:

```python
with open("foo.txt") as fo:
    for line in fo:
        print(line)

------
Output:  
Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.
```

Read lines into the list

```python
with open("foo.txt") as fo:
    lines = fo.readlines()
    print(lines)

------
Output:  
['Explicit is better than implicit.\n', 'Simple is better than complex.\n', 'Complex is better than complicated.\n', 'Flat is better than nested.']
```

## File handling

```python
import os
# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt")
```

```python
import os
# Delete file test2.txt
os.remove("text2.txt")
```

## Directory

![[files_directory.png]]

```python
import os

# print current path
print(os.getcwd())

# change current dir to /tmp
 os.chdir("/tmp")

# create new directory
os.mkdir("app_dir")

# delete directory
os.rmdir("app_dir")
```

# Next Notes

[[Packages]]