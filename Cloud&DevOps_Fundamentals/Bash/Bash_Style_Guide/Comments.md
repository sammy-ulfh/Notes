# Index

- [[#Comments]]
	- [[#File header]]
	- [[#Function comments]]
	- [[#Implementation comments]]
	- [[#Todo comments]]
- [[#Next Notes]]
# Comments

## File header

Start each file with a description of its contents.

Every file must have a top-level comment including a brief overview of its contents. A copyright notice and author information are optional.

Example:

```shell
#!/bin/bash
#
# Perform hot backups of Oracle databases.
```

## Function comments

Any function that is not both obvious and short must be commented. Any function in a library must be commented regardless of length or complexity.

It should be possible for someone else to learn how to use your program or to use a function in your library by reading the comments (and self-help, if provided) without reading the code.

All function comments should describe the intended API behaviour using:

- Description of the function.
- Globals: List of global variables used and modified.
- Arguments: Arguments taken.
- Outputs: Output to STDOUT or STDERR.
- Returns: Returned values other than the default exit status of the last command run.

```shell
#######################################
# Cleanup files from the backup directory.
# Globals:
#   BACKUP_DIR
#   ORACLE_SID
# Arguments:
#   None
#######################################
function cleanup() {
  …
}

#######################################
# Get configuration directory.
# Globals:
#   SOMEDIR
# Arguments:
#   None
# Outputs:
#   Writes location to stdout
#######################################
function get_dir() {
  echo "${SOMEDIR}"
}

#######################################
# Delete a file in a sophisticated manner.
# Arguments:
#   File to delete, a path.
# Returns:
#   0 if thing was deleted, non-zero on error.
#######################################
function del_thing() {
  rm "$1"
}
```

## Implementation comments

Comment tricky, non-obvious, interesting or important parts of your code.

This follows general Google coding comment practice. Don't comment everything. If there's a complex algorithm or you're doing something out of the ordinary, put a short comment in.

## Todo comments

Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.

TODOs should include the string TODO in all caps, followed by the name, e-mail address, or other identifier of the person with the best context about the problem referenced by the TODO. The main purpose is to have a consistent TODO that can be searched to find out how to get more details upon request. A TODO is not a commitment that the person referenced will fix the problem. Thus when you create a TODO, it is almost always your name that is given.

Examples:
```shell
# TODO(mrmonkey): Handle the unlikely edge cases (bug ####)
```

# Next Notes

[[Formating]]