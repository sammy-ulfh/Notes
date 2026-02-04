# Index

- [[#Archiving]]
	- [[#Easiest way of archiving]]
- [[#Next Notes]]
# Archiving

```python
import os
import zipfile

with zipfile.ZipFile("file.zip", "w") as zf:
    for dirpath, dirnames, files in os.walk("any_directory"):
        zf.write(dirpath)
        for filename in files:
            zf.write(os.path.join(dirpath, filename))

with zipfile.ZipFile('file.zip', 'r') as zf:
    zf.extractall(path='extract_dir')
```

```python
import tarfile # library for tar archives processing
```

## Easiest way of archiving

```python
import shutil

# shutil.make_archive(base_name, format, root_dir)
shutil.make_archive('data/backup', 'zip', 'data/')

shutil.unpack_archive('backup.tar', 'extract_dir/')
```

# Next Notes

[[Docker essentials]]