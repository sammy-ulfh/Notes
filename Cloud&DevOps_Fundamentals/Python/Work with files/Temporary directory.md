# Index

- [[#Temporary directory]]
- [[#Next Notes]]
# Temporary directory

```python
import tempfile
with tempfile.TemporaryDirectory() as tmpdir:
     print('Created temporary directory ', tmpdir)
     # Created temporary directory, e.g. /tmp/tmpoxbkrm6c
     print(os.path.exists(tmpdir))
     # True

# Directory contents have been removed
os.path.exists(tmpdir)
# False
```

# Next Notes

[[Traversing directory]]