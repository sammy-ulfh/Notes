# Index

- [[#Loops]]
	- [[#Usage]]
	- [[#Break]]
	- [[#Continue]]
	- [[#else in loops]]
- [[#Next Notes]]
# Loops

![[loops.png]]

## Usage

__While__:

```python
i = 10
while i > 0:
    print(i)
    i -= 1
```

__for__:

```python
for i in range(10):
    print(i)
```

__one-line (list comprehesion)__:

```python
l = [i for i in range(10)]
print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Break

The **break** statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.

```python
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")  
  
------  
Output:  
s  
t  
r  
The end
```

## Continue

The **continue** statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.

```python
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")  
  
------  
Output:  
s  
t  
r  
n  
g  
The end
```

## else in loops

__While__:

In Python, the **while** statement may have an optional else clause:

```python
while i > 0:
    print(i)
    i -= 1
else: # i > 0 == False
    print("End")
```

In this syntax, the condition is checked at the beginning of each iteration. The code block inside the while statement will execute as long as the condition is **True**.

When the condition becomes **False** and the loop runs normally, the else clause will execute. However, if the loop is terminated prematurely by either **break** or **return** statement, the **else** clause won’t execute at all.

The following flowchart illustrates the while...else clause:

![[Python-while-else.png]]

__for__:

```python
for i in range(5):
    print(i)
else: # end of iteration
    print("End")  
  
------  
Output:  
0  
1  
2  
3  
4  
End
```

```python
for i in range(4):
    print(i)  
    break
else: # end of iteration
    print("End")
```

```
------  
Output:  
0
```

# Next Notes

[[Numbers]]