# Index

- [[#Filename pattern]]
- [[#Next Notes]]
# Filename pattern

```python
import fnmatch
import os

for filename in os.listdir('.'):
     if fnmatch.fnmatch(filename, 'data_*_backup.txt'):
         print(filename)
```

# Next Notes

[[Traversing directory]]