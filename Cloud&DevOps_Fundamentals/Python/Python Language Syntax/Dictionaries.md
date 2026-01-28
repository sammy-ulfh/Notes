# Index

- [[#Dictionaries]]
	- [[#Acces to dict items]]
	- [[#Update dict]]
	- [[#Delete dict items]]
	- [[#Restrictions on Dictionary Keys]]
	- [[#Built-in functions]]
	- [[#Dictionary methods]]
- [[#Next Notes]]
# Dictionaries

Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value:

```python
dict0 = {}
dict1 = {'abc': 456 }
dict2 = {'abc': 123, 98.6: 37 }
dict3 = {'Alice': '2341', 'Beth': '9102'}
```

## Acces to dict items

```python
>>> d = {'Name':'Zara' ,'Age':7, 'Class':'First'}
>>> print("d['Name']: ", d['Name'])
d['Name']:  Zara

>>> print("d['Age']: ", d['Age'])
d['Age']:  7

>>> print("d['Alice']: ", d['Alice'])
KeyError: 'Alice'
```

## Update dict

```python
>>> d = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

>>> d['Age'] = 8               # update existing entry
>>> d['School'] = "DPS School" # Add new entry

>>> print("d['Age']: ", d['Age'])
d['Age']:  8
>>> print("d['School']: ", d['School'])
d['School']:  DPS School
```

## Delete dict items

```python
d = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del d['Name'] # remove entry with key 'Name‘
d.clear()     # remove all entries in dict
del d         # delete entire dictionary

print("d['Age']: ", d['Age'])
# NameError: name 'd' is not defined
```

## Restrictions on Dictionary  Keys

- __uniqueness__

```python
>>> d = {'Name': 'Zara',  'Name': 'Manni'}
>>> print("d['Name']:", d['Name'])
d['Name']: Manni
```

- __immutable__

```python
d = {['Name']: 'Zara', 'Age': 7}
print("d['Name']:", d['Name'])
# TypeError: unhashable type: 'list'
```

## Built-in functions

![[dict_built-in_function.png]]

## Dictionary methods

__clear(): Remove all items from the dictionary__

```python
>>> dict1 = {'name': 'Tom', 'age': 7}
>>> dict1.clear()
>>> dict1
{}
```

__copy(): Return a shallow copy of the dictionary__

```python
>>> dict1 = {'name': 'Tom', 'age': 7}
>>> dict2 = dict1.copy()
>>> dict2['name'] = 'Bob'
>>> print(dict1, dict2)
{'name': 'Tom', 'age': 7} {'name': 'Bob', 'age': 7}
```

__Example: _setdefault_(key[,default]):__

If key is in the dictionary, return its value;
If not, insert key with a value of default and return default.

```python
# Anti-pattern
d = {}

if "node" not in d:
    d["node"] = []

d["node"].append("item")

# Best practice
d = {}
d.setdefault("node", []).append("item")
```

__Iterate through dict items: items(),keys(),values()__

```python
d = {'name': 'Tom', 'age': 27}
for key in d:  # == for key in d.keys()
    print(key, sep=' ')  # name age
if 'name' in d:
    print(d['name']  # Tom
```

```python
for value in d.values():
    print(value, sep=' ')  # Tom 27
```

```python
for key, value in d.items():
   print(key, value)
# name Tom
# age 27
```

__fromkeys(iterable[,value]): Create a new dict with keys from iterable and values set to value.__

```python
>>> dict1 = dict.fromkeys(['one', 'two', 3])
>>> dict1
{'one': None, 'two': None, 3: None}
>>> dict2 = dict.fromkeys(['one', 'two', 3], 10)
>>> dict2
{'one': 10, 'two': 10, 3: 10}
```

__get_(key\[,default]): Return the value for key if key is in the dictionary, else default.__

```python
>>> d = {'name': 'Tom', 'age': 27}
>>> print("My name is %s" % d.get('name'))
My name is Tom
>>> print("I'm working for %s" % d.get('job', 'YOU'))
I’m working for YOU
```

__pop(key[,default]): Remove key and return its value, else return default.__

```python
>>> d = {1: 'a', 2: 'b'}
>>> d.pop(2)
'b'
>>> d
{1: 'a'}
>>> d.pop(3, 'c')
'c'
>>> d.pop(4) # KeyError
```

__popitem(): Remove and return a (key, value) pair from dict. Pairs are returned in LIFO order.__

```python
>>> d = {"one": 1, "two": 2, "three": 3, "four": 4}
>>> print(d.popitem())
('four', 4)
```

__Example: _update_(dict):__

Update the dictionary with the key/value pairs from other.

```python
>>> d1 = {1: "one", 2: "three"}
>>> d2 = {2: "two"}
>>> d1.update(d2) # updates the value of key 2
>>> d1
{1: 'one', 2: 'two'}
>>> d2 = {3: "three"}
>>> d1.update(d2) # adds element with key 3
>>> d1
{1: 'one', 2: 'two', 3: 'three'}
```

See also [https://docs.python.org/3/tutorial/datastructures.html#dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

# Next Notes

[[Sets]]