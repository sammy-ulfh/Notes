# Index

- [[#Working with data]]
	- [[#Immutable vs Mutable]]
- [[#Next Notes]]
# Working with data

In syntax and code descriptions, **square brackets** (**[ ]**) are used for notational purposes only. To avoid syntax errors, do not include them when entering a command or writing code.

Square brackets indicate **optional parts** of a statement. They should not be entered.

In many cases, items in the square brackets are optional because default values are provided.

__Multiline assignments__

```python
a = b = c = 1
a, b, c = 1, 2, "john"
```

__Deleting variables__

`del var1[, var2[, var3[...., varN]]] # syntax description`

Example:

```python
a = 1  
b = 2  
c = "Hello"  
del a  
del b, c  
print(a) # NameError: name is not defined
```

__Type conversion__

- `int(x [,base])` - returns an integer object constructed from a number or string
- `float(x)` - returns a floating-point object constructed from a number or string
- `str(x)` - returns a string version of an object

## Immutable vs Mutable

All the data in a Python code is represented by objects or by relations between objects. Every object has an **identity**, a **type**, and a **value**.

__Identify__

An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The is operator compares the identity of two objects; the **id()** function returns an integer representing its identity.

__Type__

An object’s type defines the possible values and operations (e.g. “does it have a length?”) that type supports. The `type()` function returns the type of an object. An object type is unchangeable like the identity.

__Value__

The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable.

The mutability of an object is determined by its type.

**Immutable**: int, float, string, tuple

```python
x = 'foo'
y = x
print(x) # foo
```

![[mutable1.png]]

```python
y += 'bar'
print(x) # foo
```

![[mutable2.png]]

**Mutable**: list, dict, object, set

```python
x = [1, 2, 3]
y = x
print(x) # [1, 2, 3]
```

![[mutable3.png]]

```python
y += [3, 2, 1]
print(x) # [1, 2, 3, 3, 2, 1]
```

![[mutable4.png]]

Use [https://pythontutor.com/](https://pythontutor.com/) to visualize the memory usage of your code.

# Next Notes

[[Operators]]