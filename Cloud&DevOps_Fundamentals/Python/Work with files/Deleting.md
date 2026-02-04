# Index

- [[#Deleting]]
- [[#Next Notes]]
# Deleting

```python
import os

if os.path.isfile(data_file):
    os.remove(data_file)
else:
    os.rmdir(data_file) # remove empty directory
```

```python
import shutil

trash_dir = 'my_documents/bad_dir'
try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
```
# Next Notes

[[Copying and moving]]