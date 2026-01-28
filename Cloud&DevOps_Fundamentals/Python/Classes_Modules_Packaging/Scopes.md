# Index

- [[#Scopes]]
	- [[#Global vs local variables]]
	- [[#Global]]
	- [[#Name Resolution The LEGB rule]]
	- [[#Anonymous function - lambda]]
	- [[#globals() and locals()]]
- [[#Next Notes]]
# Scopes

## Global vs local variables

**Global** variables are those which are not defined inside any function and have a global scope whereas **local** variables are those which are defined inside a function and their scope is limited to that function only. In other words, we can say that local variables are accessible **only inside the function** in which it was initialized whereas the global variables are accessible **throughout the program** and inside every function. Local variables are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function.

```python
total = 0  # Global

def sum(arg1, arg2):
    """Add both the parameters and return them."""
    total = arg1 + arg2 # Local
    print("Inside the function:", total)
    return total

sum(10, 20)
print("Outside the function:", total)  
  
------  
Output:  
Inside the function: 30  
Outside the function: 0
```

## Global

We only need to use the `global` keyword in a function if we want to do assignments or change the global variable. global is not needed for printing and accessing variables. Python “assumes” that we want a local variable due to the assignment to money inside of add_money(). Any variable which is changed or created inside of a function is local if it hasn’t been declared as a global variable. To tell Python, that we want to use the global variable, we have to use the keyword “global”, as can be seen in the following example:

```python
money = 2000

def add_money():
    # Uncomment to fix
    # global money
    money = money + 1
    print(money)

add_money()
print(money)
```

## Name Resolution: The LEGB rule

The concept of scope rules how variables and names are looked up in your code. It determines the visibility of a variable within the code. The scope of a name or variable depends on the place in your code where you create that variable. The Python scope concept is generally presented using a rule known as the **LEGB rule**.

The letters in the acronym LEGB stand for Local, Enclosing, Global, and Built-in scopes. This summarizes not only the Python scope levels but also the sequence of steps that Python follows when resolving names in a program.

![[LEGB_Rule.png]]

## Anonymous function - lambda

__lambda \[arg1 \[,arg2,.....argn]]:expression__

A **lambda** **function** is a small **anonymous** **function**. A lambda function can take any number of arguments, but can only have one expression.

```python
# Function definition
sum = lambda a, b: a + b

# Sum as a function
print("sum :", sum(10, 20)) # to call a function you should use () after its name
print("sum :", sum(20, 20))
```

## globals() and locals()

The `globals()` function returns a dictionary containing the variables defined in the global namespace. 

The `locals()` function returns a dictionary containing the variables defined in the local namespace.

```python
>>> q = lambda: locals()
>>> q()
{}
>>> def q():
...     qwert = 1
...     print(locals())
...
>>> q()
{'qwert': 1}
```

# Next Notes

[[Class]]