# Index

- [[#Tuples]]
	- [[#Initialization]]
	- [[#Access to elements / slices]]
	- [[#Update]]
	- [[#Operations]]
- [[#Next Notes]]
# Tuples

## Tuple (immutable)

## Initialization

A __tuple__ is a collection of objects which ordered and immutable. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

```python
tup0 = ()

tup1 = ('physics', 'chemistry', 1997, 2000)

tup2 = (1, 2, 3, 4, 5 )

tup3 = "a", "b", "c", "d"
```

## Access to elements / slices

```python
>>> t = tuple(i for i in range(16))
>>> t
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
>>> t[10:]
(10, 11, 12, 13, 14, 15)
>>> t[:10]
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> t[:10:2]
(0, 2, 4, 6, 8)
>>> t[10::-1]
(10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
>>> t[::-1]
(15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

## Update

```python
>>> tup1 = (12, 34.56)
>>> tup2 = ('abc', 'xyz')

>>> tup1[0] = 100
TypeError: 'tuple' object does not support item assignment

>>> tup3 = tup1 + tup2
>>> print(tup3)
(12, 34.56, 'abc', 'xyz')
```

## Operations

![[tuple_operations.png]]

# Next Notes

[[Dictionaries]]

