
# Index

- [[#Directory listing]]
- [[#Next Notes]]
# Directory listing

```python
import os

with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name)
```
# Next Notes

