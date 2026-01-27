
# Index

- [[#Operators]]
	- [[#Arithmetic operators]]
	- [[#Assignment operators]]
	- [[#Comparison operators True or False]]
	- [[#Comparison operators True or False]]
	- [[#Membership operations]]
	- [[#Identify operators]]
- [[#Next Notes]]
# Operators

![[operators.png]]

## Arithmetic operators

![[arithmetics_operators.png]]
```python
>>> a = 4
>>> b = 3
>>> +a
4
>>> -b
-3
>>> a + b
7
>>> a - b
1
>>> a * b
12
>>> a / b
1.3333333333333333
>>> a % b
1
>>> a ** b
64
```

## Assignment operators

![[assignment_operators.png]]

```python
>>> a = 4
>>> b = 3
>>> a += b  
>>> print(a)
7
```

## Comparison operators: True or False

![[comparison_operators.png]]

```python
>>> a = 4
>>> b = 3
>>> a != b
True
>>> a == b
False
>>> a > b
True
>>> a < b
False

>>> a >= b
True
>>> a <= b
False
```

## Membership operations

![[membership_operators.png]]

```python
>>> s = 'Hello, world!'
>>> 'world' in s
True
```

## Identify operators

![[identity_operators.png]]

Identity operators are used to compare the objects if both the objects are actually of the same data type and share the same memory location.

```python
>>> x = 1000  # int is immutable type
>>> y = 1000
>>> x == y
True
>>> x is y
False
>>> id(x), id(y)
(4461203152, 4461203216)
```

# Next Notes

[[Python/overview/Conditions|Conditions]]