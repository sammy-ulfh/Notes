# Index

- [[#PDB]]
	- [[#Python debugger]]
	- [[#python -m pdb debug.py]]
	- [[#pdb commands]]
	- [[#pdb.set_trace()]]
- [[#Next Notes]]
# PDB

## Python debugger

Let's use a small script for debugging:

```python
#debug.py

a = "aaa"
b = "bbb"
c = "ccc"
final = a + b + c
print(final)
```

## python -m pdb debug.py

Python has an embedded command line debugger. It is convenient to use it in environments without GUI installed (for instance, inside a docker container).

`$ python -m pdb debug.py`  
`> /home/user/debug.py(1)<module>()`  
`-> a = "aaa"`

## pdb commands

![[pdb_debug.png]]

`$ python -m pdb debug.py`  
`> /home/auser/projects/devops/debug.py(1)<module>()`  
`-> a = "aaa"`

**n(ext) and s(tep)**

Continue execution until the next line in the current function is reached or it returns. (The difference between `**next**` and `**step**` is that `step` stops inside a called function, while next executes called functions at (nearly) full speed, only stopping at the next line in the current function.)

`(Pdb) n`  
`> /home/auser/projects/devops/debug.py(2)<module>()`  
`-> b = "bbb"`  
`(Pdb) s`  
`> /home/auser/projects/devops/debug.py(3)<module>()`  
`-> c = "ccc"`

**p(rint)**

Evaluate the expression in the current context and print its value.

`(Pdb) p a,b`  
`('aaa', 'bbb')`

**c(ontinue)**

Continue execution, only stop when a breakpoint is encountered.

`(Pdb) c`  
`aaabbbccc`  
`The program finished and will be restarted`  
`> /home/user/debug.py(1)<mdule>()`  
`-> a = "aaa"`

**q(uit)**

Quit from the debugger. The program being executed is aborted.

`(Pdb) q`  

## pdb.set_trace()

pdb.set_trace() inserts breakpoint in the current position.

```python
#debug.py
import pdb
a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = a + b + c
print(final)
```

Script execution will be stopped and pdb mode is enabled when Python interpreter reaches the line with the breakpoint.

`$ python debug.py`  
`> /home/user/debug.py(4)<module>()`  
`-> b = "bbb"`  
`(Pdb)`

# Next Notes

[[Jija2 templates]]