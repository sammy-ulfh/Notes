# Index

- [[#Input and output from console]]
	- [[#input( [prompt]), print]]
- [[#Next Notes]]
# Input and output from console

## input(\[prompt]), print

```python
>>> l = list(map(int, input('--> ').split()))
--> 1 2 3 4
>>> print(' '.join([str(i) for i in l]))
1 2 3 4
>>> print(*l)
1 2 3 4
>>> print(l)
[1, 2, 3, 4]

>>> import json
>>> d = json.loads(input('Input dict:'))
Input dict:{1: 'one', 2: 'two'}
>>> print(d) 
{1: 'one', 2: 'two'}
```

# Next Notes

[[Scopes]]
