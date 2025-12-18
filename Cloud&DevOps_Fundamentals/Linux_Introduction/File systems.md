
# Index

- [[#File systems]]
	- [[#Unix/Linux]]
	- [[#Windows]]
	- [[#Linux directory structure]]
	- [[#Inodes]]
	- [[#Hard link]]
	- [[#Soft link]]
- [[#Next Notes]]

# File systems

## Unix/Linux

- Supports a lot of file system types: ext2, ext3, ReiserFS, etc.
- Single hierarchy (tree) concept used  - there is one __root/__ directory, and every file existing on the system is located under it somewhere.
- There is no concept filename.extension - system doesn't make any assumptions about the file content by its extension (extension is optional).

## Windows

- Support NFTS, FAT16 & FAT32 file systems only.
- Uses a drive letter abstraction - files are located on disks (or partitions) represented by letters (A:, B:, C:, .... Z:).
- System behaviour related to file format and its content bases on it's extension (.exe is an executable file, .txt is a text file, etc).

## Linux directory structure

![[directory_structure.png]]

## Inodes

- The inode (Index Node) is a data structure in Unix-style file system that describes a file-system object such as a file or a directory. Each inode store the attributes and disk block location(s) of the object's data. File-system object attributes may include metadata (times of last change, access, modification), as well as owner and permission data.
- Directories are lists of names assigned to inodes. A directory contains an entry of itself, its parent, and each of its children.

![[inode.png]]

## Hard link

- A direct pointer to an inode because __hard links__ point to an inode, and inodes are only unique within a particular fyle system, hard links cannot cross file systems.
- Indistinguishable from original file (any changes made in the linked file reflect in the original final).
- Changes made in any reflect in all.
- A file is accessible as long as hard link to it remains.
- Created with the __ln__ command (and no options) or the link function.

## Soft link

- A symbolic link (or symlink or soft link) is a pointer to a file name.
- If the original file is moved, the link becomes invalid.
- Deleting the link does not delete the original file.
- If removed, the original file will remain.
- Usually made to directories to create shortcuts.
- Created with the __-s__ option to __ln__ or the symlink function.

# Next Notes

[[LVM]]
