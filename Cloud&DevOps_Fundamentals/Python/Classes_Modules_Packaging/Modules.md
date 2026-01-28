# Index

- [[#Modules]]
	- [[#_import_ module1 [, module2 [,... moduleN]]]
	- [[#import as]]
	- [[#import name1 as new_name [, ... ]]]
	- [[#if _ _name _ _ == " _ _main _ _"]]
	- [[#Search order]]
	- [[#dir]]
- [[#Next Notes]]
# Modules

A **module** is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable `__name__.`

```python
# hello.py
def print_module_name():
    print(f"name of module: {__name__}")
```

import
## _import_ module1\[, module2\[,... moduleN]

```python
# Import module hello
import hello

# Call function defined in that module
hello.print_module_name()

------
Output:
name of module: hello
```

There is a variant of the `import` statement that imports names from a module directly into the importing module’s namespace.

_from ... import_ name1\[, name2\[, ... nameN]]

```python
# Import from module hello
from hello import print_module_name
# Also can be used from … import *. In this case, all variables and fucntions are imported
    
# Call function defined in that module
print_module_name()
```

## import as

Sometimes, it is convenient to use alies instead of the name of the module. 
### import name1 as new_name\[, ... ]

```python
# Import module hello
import hello as bye

# Call function defined in that module
bye.print_module_name()
```

## if \_\_name\_\_ == "\_\_main\_\_"

When a Python module or package is imported, `__name__` is set to the module’s name. This is the name of the Python file itself without the .py extension.

However, if the module is executed in the top-level code environment (`python some_module.py`), its **__name__** is set to the string `'__main__'`.

```python
# main.py
print("Always executed")

if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported")
```

__Run script__:

```python
$ python main.py
Always executed
Executed when invoked directly
```

__Import Module__

```python
>>> import main
Always executed
Executed when imported
```

Some modules contain code that is intended for script use only, like parsing command-line arguments or fetching data from standard input. If a module like this was imported from a different module, for example to unit test it, the script code would unintentionally execute as well.

This is where using the `if __name__ == '__main__'` code block comes in handy. Code within this block won’t run unless the module is executed in the top-level environment.

## Search order

![[module_search_order.png]]

When the interpreter executes `import` statement, it searches for module in a list of directories assembled from the following sources:

1. The directory from which the input script was run, or the current directory if the interpreter is being run interactively
2. The list of directories contained in the **PYTHONPATH** environment variable, if it is set. 
3. An installation-dependent list of directories configured at the time Python is installed

The resulting search path is accessible in the Python variable `sys.path`, which is obtained from a module named sys:

```python
>>> import sys
>>> sys.path
```

## dir

 `dir()` returns the list of names in the current local scope. It helps to introspect a module's content.
 
```python
>>> import math
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
```

# Next Notes

[[Files]]