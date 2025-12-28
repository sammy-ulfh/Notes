# Index

- [[#Text editors]]
  - [[#VI/VIM]]
  - [[#VIM modes]]
  - [[#VIM inser mode]]
  - [[#VIM Last-line Mode (Escape Mode)]]
  - [[#VI/VIM cheatsheet]]
  - [[#NANO]]
  - [[#VISUDO]]
- [[#Next Notes]]

# Text editors

Text editors are one of the most frequently used applications in Unix systems. They are used to create and edit files in plain text format.

Currently the most popular text editors are:

- vi/vim
- nano

Default editor can be set via EDITOR environment variable

## VI/VIM

The original vi (visual editor) was developed by Bill Joy in 1976 as part of BSD Unix system. Bill Joy was later one of the co-founders of sun Microsystems. vi became popular very fast within the Unix community as it provided a full screen, visual editor, which was missing before. It is still the standard text editor that is available on any Unix system.

Vim stands for VI IMproved. Ot used to be VI IMitation, but there are so many improvements that a name change was appropriate. vim is a text editor which includes almost all the commands from the Unix program __Vi__ and a lot of new ones.

To start editing simply run:

```shell
vim file_to_edit_.txt
```

Learn VIM:

```shell
vimtutor
```

- `https://www.linuxfoundation.org/blog/blog/classic-sysadmin-vim-101-a-beginners-guide-to-vim`
- `https://vim-adventures.com/`

## VIM modes

vim has tree modes:

- Command modes
- Input mode
- Last-line mode

__Vim command mode__

When vim starts up, it is in Command Mode. This mode is where vim interprets any characters we type as commands and thus does not display them in the window. In command mode, one can move around on the screen, search the document for words or phrases, delete portions of text  and move text around.

To enter into Command Mode from any other mode, it requires pressing the \[Esc] key.

- Navigation
  ![[vim_navigation.png]]
- Editing
  ![[vim_editing.png]]
- Searching
  ![[vim_seraching.png]]

## VIM inser mode

This mode enable you to insert text into the file. Everything that's typed in this mode is interpreted as input and finally, it is put in the file. The vi always starts in command mode. To enter text, you must be Insert Mode. To come in insert mode you simply type i.

## VIM Last-line Mode (Escape Mode)

Line mode is invoked by typing a colon \[:], while vim is in command mode. The cursor will jump to the last line of the screen and vim will wait for a command. This mode enables you to perform tasks such as saving files, executing commands. 

![[vim_last_line_mode.png]]

## VI/VIM cheatsheet

![[vim_cheatsheet.png]]

## NANO

__nano__ is a small and friendly text editor. Besides basic text editing, nano offers features like undo/redo, syntax coloring, interactive search-and-replace, auto indentation, line numbers, word completion, file locking, backup files, and internationalization support.

__nano__ is modeless editor. This means that all keystrokes, with the exception of Control and Meta sequences, enter text into the file being edited.

Usual way to invoke nano is:

```shell
nano file_to_edit.txt
```

- Commands are given by using the Control Key (Ctrl, shown as ^) or the Meta Key (Alt or Cmd, shown as M-)
- Text can be cut from a file, a whole line at a time, by using the Cut Text command (default key binding: ^K)
- The contents of the cutbuffer can be pasted back into the file with the uncut Text command (default key binding: ^U)
- A line of text can be copied into the cutbuffer (without cutting it) with the Copy Text command (default key binding: M-6)

## VISUDO

__visudo__ is a specialized command for safe edit of a file located at __/etc/sudoers__, the __sudo__ command is configured through this file.

> ⚠️ Never edit this file with a normal text editor! Always use visudo command instead!


Because improper syntax in the __/etc/sudoers__ file can leave you with a broken system where it is impossible to obtain elevated privileges, it is important to use the __visudo__ command to edit the file.

The __visudo__ command opens a text editor like normal, bit __it validates the syntax__ of the file upon saving. This prevents configuration errors from blocking __sudo__ operations, which may be your only way of obtaining __root__ privileges.

Traditionally, __visudo__ opens the __/etc/sudoers__ file with the __vi__ text editor. Ubuntu, however, has configured  __visudo__ to use the __nano__ text editor instead.

[Additional details about visudo and sudo configuration](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file).

# Next Notes

[[Filesystem files search]]