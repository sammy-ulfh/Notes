# Index

- [[#Conditions]]
	- [[#if... else...]]
	- [[#one-line if]]
- [[#Next Notes]]
# Conditions

## if... else...

```python
x = int(input("Input int: "))

if x < 0:
    x = 0
    print("Changed to 0")
elif x == 0:
    print("Equals 0")
elif x == 1:
    print("Equals 1")
else:
    print("> 1")
```

## one-line if

- if

```python
var = 100
if var == 100: print("Value of expression is 100")
print("Goodbye!")
```

- if... else

```python
>>> a = 10
>>> print("even" if a % 2 == 0 else "odd")
even
>>> a = 55
>>> print("even" if a % 2 == 0 else "odd")
odd
```

# Next Notes

[[Input]]
