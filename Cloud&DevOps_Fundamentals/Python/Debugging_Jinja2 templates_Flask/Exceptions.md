# Index

- [[#Exceptions]]
	- [[#Handling exceptions]]
	- [[#Exception argument]]
	- [[#Raising an exception]]
	- [[#Custom exception]]
- [[#Next Notes]]
# Exceptions

An **exception** is an error that happens during the execution of a program. Exceptions are known to non-programmers as instances that do not conform to a general rule. The name "exception" in computer science has this meaning as well: It implies that the problem (the exception) doesn't occur frequently, i.e. the exception is the "exception to the rule". Exception handling is a construct in some programming languages to handle or deal with errors automatically. Many programming languages like C++, Objective-C, PHP, Java, Ruby, Python, and many others have built-in support for exception handling.

Error handling is generally resolved by saving the state of execution at the moment the error occurred and interrupting the normal flow of the program to execute a special function or piece of code, which is known as the exception handler. Depending on the kind of error ("division by zero", "file open error" and so on) which had occurred, the error handler can "fix" the problem and the program can be continued afterward with the previously saved data.

```python
try:
   # You do your operations here;
   ......................
except Exception1:
   # If there is Exception1, then execute this block.
except Exception2:
   # If there is Exception2, then execute this block.
   ......................
else:
   # If there is no exception then execute this block. 
finally:
   # This would always be executed.
```

## Handling exceptions

```python
try:
   You do your operations here;
   ......................
except (Exception1[, Exception2[,...ExceptionN]]]) as exc:
   If there is any exception from the given exception list, 
   then execute this block.
   ......................
else:
   If there is no exception then execute this block.
```

## Exception argument

```python
# Define a function here.
def temp_convert(var):
    try:
        return int(var)
    except ValueError as argument:
        print("The argument does not contain numbers:", argument)

temp_convert("xyz")  
  
------  
Output:  
The argument does not contain numbers: invalid literal for int() with base 10: 'xyz'
```

## Raising an exception

If you want to throw an error when a certain condition occurs use `raise.`

**raise \[Exception \[, args \[, traceback]]]**

```python
def functionName(level):
    if level < 1:
        raise Exception("Invalid level! %s“ % level)
        # The code below to this would not be executed
        # if we raise the exception
```

```python
try:
    ...
except Exception as e:
    Exception handling here...
else:
    Rest of the code here...
```

## Custom exception

```python
class Networkerror(RuntimeError):
    def __init__(self, message):
        self.message = message
```

```python
try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print(e.message)  
  
------  
Output:Bad hostname
```

# Next Notes

[[Debugging]]