# Index

- [[#Permission Model]]
  - [[#Change directory's user owner]]
  - [[#Chage the directory's group owner]]
  - [[#Access permissions]]
  - [[#Access permissions octal numerical representation]]
  - [[#Example]]
  - [[#Change access mode]]
  - [[#Sticky bit]]
  - [[#SUID/SGID]]
  - [[#lsattr]]
  - [[#chattr]]
- [[#Next Notes]]
# Permission Model

Files and devices may be granted access based on a users ID or group (owner and group owner)

`ls -l`

![[file-perm.png]]

## Change directory's user owner

__chown__ - make user directory's owner

`# chown user /home/myfolder - Make user the owner of “/home/myfolder” directory`

## Chage the directory's group owner

__chgrp__ - make an owner group for file

`# chgrp mytestgroup test.t - Make ‘mytestgroup’ group the owner group for ‘test.t’ file`

## Access permissions 

File, directory and advice (special file) permissions are granted based on __user__, __group__ or __other__ (world) identification status.

Permission is granted (or denied) for __read__ (r), __write__ (w) and __execute__ (x) access.

## Access permissions: octal numerical representation

__r = 4__
__w = 2__
__x = 1__

### Example

Converting __rwxr-x---__ to octal, for that we need to divide in 3 groups with 3 characters in each __rwx__, __r-x__, __---__ and then convert each of them:

7 = 4 + 2 + 1 = r + w + x
5 = 4 + 1 = r + x (no write)
0 = --- = no rights

So __rwxr-x---__ is __750__ in octal.

## Change access mode

__chmod__ - change permissions for file

```
# chmod g=rw test.t - Give read and write rights to group for ‘test.t’ file
# chmod 755 test.t - Give rwxr-xr-x permission for test.t using octal form
# chmod o-r,g+w test.t
```

## Sticky bit

- The sticky bit is primarily used on shared directories.
- It is useful for shared directories such as __/var/tmp__ and __/tmp__ because users can create files, read and execute files owned by other users, but are not allowed to remove files owned by other users.
- For example if user bob creates a file named /tmp/bob, other user tom can not delete this file even when the __/tmp__ directory has permission of 777. If sticky bit is not set then tom can delete /etc/bob, as the /tmp/bob file inherits the parent directory permission1s.

```
# chmod +t somedirectory - where 1 = sticky bit
# chmod 1700 somedirectory
# chmod -t somefile - - where the zero would mean no sticky bit
# chmod 0700 somefile
```

## SUID/SGID

Set-user Identification (SUID) and set-group identification (SGID)

- The setuid permission displayed as an "s" in the owner's execute field
- When a command or script with SUID bit set is run, its effective UID becomes that of the owner of the file, rather than of the users who is running it.
- To set SUID on a file.

```
chmod 4555 [path_to_file]
```

The setgid permission displays as an "s" in the group's execute field.

- SGID permission is similar to the SUID permission, only difference is - when the script or command with SGID on is run, it runs as if it were a member of the same group in which the file is a member.
- To set SGID on a folde

```
# chmod 2555 [path_to_folder]
```

## lsattr

This will list if whether a file has any special attributes (as set by chattr). Use the -R option to list recursively and try using the -d option to list directories like other files rather than listing their contents. Command syntac:

`# lsattr`

This will list files in the current directory, you may also like to specify a directory or file:

`# lsattr /directory/or/file`

## chattr

Change file system attributes

- __i__: sets the __immutable__ flag on a file - will prevent any changes (accidental or otherwise) to the "lilo.conf" file. If you wish to modify the lilo.conf file, you will need to unset the immutable flag: chattr -i.
  `# chattr +i /sbin/lilo.conf`
- __A__: sets no access time flag - if a file or directory has this attribute set, whenever it is accessed, either for reading of for writing, it's last access time will nor be updated . This can be useful, for example, on files or directories which are very often accessed for reading, especially since this parameter is the only one which changes on an inode when it's opened.
- __a__: sets append only flag - if a file has this attribute set and is open for writing, the only operation possible will be to append data to it's previous content. For directory, this means that you can only add files to it, but not rename or delete any existing file.
- __s__: sets secure deletion flag - when such a file or directory with this attribute set is deleted, the blocks is was occupying on disk are written back with zeroes (similar to using shred).
- [Adittional examples](https://wiki.archlinux.org/title/File_permissions_and_attributes)

# Next Notes

[[SELinux]]