# Index

- [[#Strings]]
	- [[#Strings formatting]]
	- [[#Different strings]]
	- [[#Methods]]
- [[#Next Notes]]
# Strings

Strings in python support indexing and slicing. To extract a single character from a string, follow the string with the index of the desired character surrounded by square brackets (\[ ]), remembering that the first character of a string has index **zero**.

```python
>>> what = 'This parrot is dead'
>>> what[3]
's'
>>> what[0]
'T'
```

If the subscript you provide between the brackets is less than zero, python counts from the end of the string, with a subscript of -1 representing the last character in the string.

```python
>>> what[-1]
'd'
```

To extract a contiguous piece of a string (known as a **slice**), use a subscript consisting of the starting position followed by a colon (:, finally followed by one more than the ending position of the slice you want to extract. Notice that the slicing stops immediately before the second value:

```python
>>> what[0:4]
'This'
>>> what[5:11]
'parrot'
```

One way to think about the indexes in a slice is that you give the starting position as the value before the colon, and the starting position plus the number of characters in the slice after the colon.

For the special case when a slice starts at the beginning of a string or continues until the end, you can omit the first or second index, respectively. So to extract all but the first character of a string, you can use a subscript of 1: .

```python
>>> what[1:]
'his parrot is dead'
```

To extract the first 3 characters of a string you can use :3 .

```python
>>> what[:3]
'Thi'
```

If you use a value for a slice index that is larger than the length of the string, python does not raise an exception, but treats the index as if it was the length of the string.

Also, it is possible to define step in slice:

```python
>>> what[1:-1:2]
'hspro sda'
```

Copy of string:

```python
>>> copy = what[:]
>>> copy
'This parrot is dead'
```

Revert string

```python
>>> what[::-1]
'daed si torrap sihT'
```

## Strings formatting

```python
a, b = 1, 2
print(f"{a}+{b}={a+b}") # 1+2=3
  
print("String: %s integer %d" % ('str', 57)) # String: str integer 57
print("list: %s" % [1,2,3]) # list: [1, 2, 3]

print('{0} and {1}'.format('minced meat', 'eggs')) # minced meat and eggs
print('This {food} — {adjective}.'.format(food='stuffing',
                                          adjective='awful'))
# This stuffing — indescribably awful.
print('The story about {0}e, {1}y, и {other}y.'.format(
    'Billi','Manfred', other='Georg'))
# The story about Billie, Manfredy, и Georgy.
```

## Different strings

- r'expression'

```python
>>> print('C:\\nowhere')
C:\nowhere

>>> print(r'C:\\nowhere')
C:\\nowhere
```

In Python, strings prefixed with r , such as r'...' , are called **raw strings** and treat backslashes \ as literal characters. Raw strings are useful when handling strings that use a lot of backslashes, such as Windows paths and regular expression patterns.

## Methods

![[methods.png]]

See [https://docs.python.org/3/library/string.html](https://docs.python.org/3/library/string.html) for additional information

# Next Notes

[[Lists]]