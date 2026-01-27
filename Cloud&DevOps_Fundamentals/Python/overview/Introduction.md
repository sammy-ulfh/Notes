# Index

- [[#Python Introduction]]
	- [[#The pros of Python]]
	- [[#The cons of Python]]
	- [[#Enable interactive mode]]
	- [[#Executing Python Code]]
	- [[#Exiting the interpreter]]
- [[#Next Notes]]

# Python Introduction

__Python__ is a [High-level](https://en.wikipedia.org/wiki/High-level_programming_language), [interpreted](https://en.wikipedia.org/wiki/Interpreter_(computing)), [general-purpose programming language](https://en.wikipedia.org/wiki/General-purpose_programming_language). Its design philosophy emphasizes [code readability](https://en.wikipedia.org/wiki/Code_readability) with the use of [significant indentation](https://en.wikipedia.org/wiki/Off-side_rule).

Python is [dynamically-typed](https://en.wikipedia.org/wiki/Type_system#DYNAMIC) and [garbage-collected](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)) (automatic memory management). It supports multiple [programming paradigms](https://en.wikipedia.org/wiki/Programming_paradigm), including [structured](https://en.wikipedia.org/wiki/Structured_programming) (particularly [procedural](https://en.wikipedia.org/wiki/Procedural_programming)), [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) and [functional programming](https://en.wikipedia.org/wiki/Functional_programming). Its often described as a "batteries included" language due to its comprehensive [standard library](https://en.wikipedia.org/wiki/Standard_library). Python consistently ranks as one of the most popular programming languages.

![[PythonForDevOps.png]]

## The pros of Python

- Easy to learn
- Readability
- High-level language
- Developer productivity
- Cross-platform. Portable
- Batteries included: Python has a vast collection of libraries
- Widely Supported
- Enjoyment

## The cons of Python

- Speed Limitations
- Memory consumption
- Requires more testing


Python is an interpreted, dynamic language. The Python interpreter can be used in two modes: __interactive__ and __scripted__. In __interactive mode__, Python responds to each statement while we type. In __script mode__, we give Python a file of statements and turn it loose to interpret all of the statements in that script. Both modes produce identical results.

## Enable interactive mode

Python comes preinstalled on most Linux distributions. In order to get into interactive mode:

- Open a terminal
- Type Python
- Press the Enter Key

If you are seeing the prompt, you're off and and running!


## Executing Python Code

The next step is to execute the statement that displays Hello, World! to the console:

- Ensure that the >>> prompt is displayed, and the cursor is positioned after it.
- Type the command __print("Hello, World!")__ exactly as shown.
- Press the Enter Key.

The interpreter's response should appear on the next line. You can tell it is console output because the >>> prompt is absent:

```python
>>> print("Hello, World!")
Hello, World!
```

## Exiting the interpreter

Type exit() and press the Enter key. Or type Ctrl+D.

__The Zen of Python__ is a collection of 19 "guiding principles" for writing computer programs that influence the design of the Python programming language. Software engineer Tim Peters wrote this set of principles and posted it on the Python mailing list in 1999.

The write of the Zen of Python, long-time Pythoneer Tim Peters left the 20th rule empty. His idea was for Guido to contribute number twenty, but that never happened.

A little Easter egg that has been present in Python for a long time lists the Zen of Python. You can trigger the easter egg by importing the module this.

Start Python in interactive Mode and type __import__ this:

```shell
$ python
>>> import this
```

The Zen of Python principles:

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparce is better than dense.
- Readability counts.
- Special cases aren't special enough to break the rules.
- Although practically beats purity.
- Errors should never pass silently.
- Unless explicitly silenced.
- In the face of ambiguity, refuse the temptation to guess.
- There should be one and preferably only one, obvious way to do it.
- Although that way may not be obvious at first unless you're Dutch.
- Now is better than ever.
- Although never is often better than __right__ now.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.
- Namespaces are one honking great idea -- let's do more of those!

You should follow these principles during developing Python scripts.

# Next Notes

[[History]]