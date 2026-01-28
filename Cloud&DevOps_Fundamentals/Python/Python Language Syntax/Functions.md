# Index

- [[#Functions]]
	- [[#Function declaration]]
	- [[#Function call]]
	- [[#Arguments by reference]]
	- [[#Arguments]]
	- [[#Positional and keyword argument]]
- [[#Next Notes]]
# Functions

## Function declaration

- def + name + () + :
- Arguments -> ()
- 1 expression can be a documentation
- Indentation
- return == return None
- if return is skipped == return None

```python
def function_name(parameters):
    ”””function_docstring“””
    function_suite
    return [expression]
```

## Function call

```python
# Function definition
**def printme**(str):
   """This prints a passed string."""
   print(str)

>>> printme("You have the best company!")
You have the best company!
>>> printme("Cloud & DevOps is the best department")
Cloud & DevOps is the best department
```

## Arguments by reference

By reference means that the argument you’re passing to the function is a reference to a variable that already exists in memory rather than an independent copy of that variable.

```python
def changeme(mylist):
   "This changes a passed list"
   mylist.append([1,2,3,4])
   print("Inside the function:", mylist)

mylist = [10,20,30]
changeme(mylist)
# Inside the function: [10, 20, 30, [1, 2, 3, 4]]
print("Outside the function:", mylist)
# Outside the function: [10, 20, 30, [1, 2, 3, 4]]
```

## Arguments

![[function_arguments.png]]

## Positional and keyword argument

```python
def add(a, b): return a + b

# positional: matched from left to right
add(1, 2)

# keyword: name=value syntax
add(a=1, b=2)
add(b=2, a=1)
add(1, b=2)

add(a=1, 2)
# SyntaxError: positional argument follows keyword argument
add(2, a=1)
# TypeError: add() got multiple values for argument 'a'
```

## Default argument

```python
def add(a, b=2):  # b - default
    return a + b

add(1, 2)
add(1)
add(1, b=2)
add(a=1, b=2)
add(a=1)

def add(a=1, b): return a + b
# SyntaxError: non-default argument follows default argument
```

## Arbitrary arguments lists

```python
def echo(a, b, c=3, *args, **kwargs):
    print(a, b, c, args, kwargs)

echo(1, 2)
# 1 2 3 () {}
echo(1, 2, 3)
# 1 2 3 () {}
echo(1, 2, 3, 4, 5)
# 1 2 3 (4, 5) {}
echo(1, 2, 3, 4, 5, d=6)
# 1 2 3 (4, 5) {'d': 6}
echo(1, b=2, d=6, e=7)
# 1 2 3 () {'d': 6, 'e': 7}
```

# Next Notes

[[Input and output from console]]