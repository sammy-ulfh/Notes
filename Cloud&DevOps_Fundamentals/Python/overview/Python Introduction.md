# Index

- [[#Python Introduction]]
	- [[#Python keywords]]
	- [[#Quotes in Python]]
	- [[#Indentations in python]]
	- [[#Multi-line in python]]
	- [[#Comments in Python]]
	- [[#Variable Types in Python]]
- [[#Next Notes]]
# Python Introduction

Python identifiers are user-defined names. They are used to specify the names of variables, functions, classes, modules, etc.

There are a few rules that must be followed to create a python identifier:

- You can't use __reserved keywords__ as an identifier name. If you will try, it will throw SyntaxError.
- Python identifier contain letters in a small case (a-z), and upper case (A-Z), digits (0-9), and underscore (\_).
- Identifier names can't begin with a digit. For example, 10test would be an invalid identifier.
- Python identifier can't contain only digits. For example, 888 would be an invalid identifier.
- Python identifier name can start with underscore. So, the \_test would be an invalid identifier.
- There is no limit on the length of the identifier name. But, don't try to keep a super long identifier, it will only hurt your credibilityas a programmer.
- Python identifier names are case-sensitive.
-  EPAM != epam

## Python keywords

Python keywords are special reserved words that have specific meanings and purposes and can't be used for anything but those specific purposes. These keywords are always available -- you'll never have to import them into your code. You can't use them as variable names. Otherwise, __SyntaxError__ will be raised. You will get acquainted with the majority of keywords during the course.


| False  | class    | from     | or     |
| ------ | -------- | -------- | ------ |
| None   | continue | global   | pass   |
| True   | def      | if       | raise  |
| and    | del      | import   | return |
| as     | elif     | in       | try    |
| assert | else     | is       | while  |
| async  | except   | lambda   | with   |
| await  | finally  | nonlocal | yield  |
| break  | for      | not      |        |
## Quotes in Python

Python strings are sequences of characters and numbers.

A string is wrapped around a set of **single quotes** or **double** **quotes**. There is **no difference** in which you use.

Anything that goes inside the quotes is interpreted as being "text" instead of an executable command.

```python
word = 'word'
sentence = "This is a sentence."
```

Use triple quotes for docstrings and multiline comments:

```python
paragraph = """This is a paragraph.
It is made up of multiple lines and sentences."""
```

To write a quoted string inside another string in python:

- Use doubles quotes in the outer string, and single quotes in the inner string
- Use single quotes in the outer string and double quotes in the inner string.

```python
inside_1 = "Quotation 1 'inside'."
inside_2 = 'Quotation 2 "inside".'
```

## Indentations in python

Indentation in Python is used to create a group of statements. Many popular languages such as C, and Java uses braces ({ }) to define a block of code, and Python uses indentation.

Indentation in Python refers to the whitespaces at the start of the line. We can create an indentation using **space** or **tabs**. When writing Python code, we have to define a group of statements for functions and loops. This is done by properly indenting the statements for that block.

The best practice is to use **4** whitespaces for the first indentation and then keep adding additional 4 whitespaces to increase the indentation.

```python
if a == 0:
    print("OK")
else:
    print("FAIL")
```

```python
if a == 0:
    print("OK")
      print("Done") # IndentationError, all statements in a group should have the simular identation
else:
      print("FAIL") # it is OK as it is another group. However, the best practice is to use 4 whitespaces
```

## Multi-line in python

\ - Continuation operator

You cannot split a statement into multiple lines in Python by pressing Enter. Instead, use the backslash (\\) to indicate that a statement is continued on the next line.

line continuation inside (), \[], {}

```python
total = item_one + \
        item_two + \
        item_three
```

Line continuation is automatic when the split comes while a statement is inside parenthesis ( ( ), brackets (\[ ) or braces ( { ). This is convenient, but can also lead to errors if there is no closing Parenthesis, bracket, or brace. Python would interpret the rest of the script as one statement in that case.

```python
days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
]
```

## Comments in Python

```python
# First comment
print("Hello, Python!")  # second comment
```

## Variable Types in Python

Python supports two types of numbers - integers (whole numbers) and floating point numbers (decimals). (It also supports complex numbers, which will not be explained in this course).

In Python, there is effectively no limit to how long an integer value can be. Of course, it is constrained by the amount of memory your system has, as are all things, but beyond that, an integer can be as long as you need it to be

Strings are defined either with a single quote or double quotes.

```python
counter = 100  # An integer assignment
miles = 1000.0 # A floating point
name = "John"  # A string

print(counter)
print(miles)
print(name)  
  
------  
Output:  
100  
1000.0  
John
```

In some programming languages such as Java or C#, when declaring a variable, you need to specify a data type for it.

Unlike statically-typed languages, Python is a dynamically typed language. When declaring a variable in Python, you don’t specify a type for it:

```python
message = 'Hello'
```

In Python, the `message` variable is just a reference to an object which is a string. There is no type associated with the message variable.

![[Dynamic-Typing-in-Python-example.png]]

If you assign the `message` to a number, it’s perfectly fine:

```python
message = 100
```

![[Dynamic-Typing-in-Python-example-reassignment.png]]

# Next Notes

[[Working with data]]