# Index

- [[#Scripts]]
	- [[#Python interactive console]]
	- [[#Run script]]
		- [[#Windows]]
		- [[#Unix]]
- [[#Next Notes]]
# Scripts

## Python interactive console

The most straightforward way to start talking to Python is in an interactive Read-Eval-Print Loop (__REPL__) environment. That simply means starting up the interpreter and typing commands to it directly. The interpreter:

- **R**eads the command you enter
- **E**valuates and executes the command
- **P**rints the output (if any) to the console
- **L**oops back and repeats the process

The session continues in this manner until you instruct the interpreter to terminate. Most of the example code in this tutorial series is presented as REPL interaction.

```shell
$ python
Python 3.8.11 (default, Jun  4 2021, 08:36:30)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('Hello World!')
Hello World!
>>> 2 + 5
7
>>> print('Welcome to Real Python!')
Welcome to Real Python!
```

## Run script 

### Windows 

```python
# File test.py
print("Hello, Python!")
```

```powershell
$python test.py
```

## Unix

```python
#!/usr/bin/env python
print("Hello, Python!")
```

`$python test.py` || `$./test.py`

# Next Notes

[[Editors - IDEs]]