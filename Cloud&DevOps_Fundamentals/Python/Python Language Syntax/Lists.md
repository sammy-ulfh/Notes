# Index

- [[#Lists]]
	- [[#Update items]]
	- [[#Delete items]]
	- [[#Operations]]
	- [[#Built-in functions]]
	- [[#List methods]]
- [[#Next Notes]]
# Lists

In short, a list is a collection of arbitrary objects, somewhat akin to an array in many other programming languages but more flexible. Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets ([]), as shown below:

```python
list1 = ['physics', 'chemistry', 1997, 2000]

list2 = [1, 2, 3, 4, 5 ]

list3 = ["a", "b", "c", "d"]
```

The important characteristics of Python lists are as follows:

- Lists are ordered.

```python
>>> [1, 2, 3, 4] == [4, 1, 3, 2]
False
```

- Lists can contain any arbitrary objects.
- List elements can be accessed by index. Slicing also works for lists.

```python
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
```

![[t.png]]

Lists can be nested to arbitrary depth.   
A list can contain any number of objects, from zero to as many as your computer’s memory will allow.

```python
>>> x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
```

![[nested.png]]

```python
>>> x[1]
['bb', ['ccc', 'ddd'], 'ee', 'ff']
>>> x[1][0]
'bb'
>>> x[1][1]
['ccc', 'ddd']
>>> x[1][2]
'ee'
>>> x[1][3]
'ff'
>>> x[3]
['hh', 'ii']
>>> print(x[3][0], x[3][1])
hh ii
```

Lists are mutable.

## Update items

```python
>>> list1 = ['physics', 'chemistry', 1997, 2000]
>>> print(list1[2])
1997
>>> list1[2] = 2001
>>> print(list1[2])
2001
```

## Delete items

```python
>>> list1 = ['physics', 'chemistry', 1997, 2000]
>>> print(list1)
['physics', 'chemistry', 1997, 2000]
>>> del list1[2]
>>> print(list1)
['physics', 'chemistry', 2000]
```

## Operations

![[operations.png]]

## Built-in functions

![[built-in_functions.png]]

## List methods

__append (value): Append an item to the list__

```python
>>> numbers = [1, 2]
>>> numbers.append(3)
>>> numbers
[1, 2, 3]
```

__count (value): Count the occurrences of a given item in the list__

```python
>>> numbers = [1, 2, 3, 3]
>>> numbers.count(3)
2
```

__extend(iterable): Extend list with the another list items__

```python
>>> numbers = [1, 2, 3]
>>> numbers.extend([4, 5, 6])
>>> numbers
[1, 2, 3, 4, 5, 6]
```

__index(value, \[start, \[stop]]): Find position of item; Raise ValueError if not found.__

```python
>>> numbers = [1, 5, 3]
>>> numbers.index(5)
1
```

__insert(index, value): Insert an item into the specified position.__

```python
>>> numbers = [1, 3]
>>> numbers.insert(1, 2)
>>> numbers
[1, 2, 3]
```

__pop(\[index = -1]): Get and remove the last (specified) item from the list.__

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers.pop()
5
>>> numbers.pop(0)
1
>>> numbers
[2, 3, 4]
```

__remove_(value): Remove the specified item from the list.__

```python
>>> numbers = [1, 2, 'a', 3, 4]
>>> numbers.remove('a')
>>> numbers
[1, 2, 3, 4]
```

__reverse(): Reverse the items of the list in place__

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers.reverse()
>>> numbers
[5, 4, 3, 2, 1]
```

__sort(cmp=None, key=None, reverse=False): Sort the items of the list in place.__

```python
>>> numbers = [1, 3, 4, 2]
>>> numbers.sort() # Sorting list of integers in ascending
>>> numbers
[1, 2, 3, 4]
>>> numbers.sort(reverse = True) # Sorting list of integers in descending
>>> numbers
[4, 3, 2, 1]
```

See [https://docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) for additional information

# Next Notes

[[Tuples]]