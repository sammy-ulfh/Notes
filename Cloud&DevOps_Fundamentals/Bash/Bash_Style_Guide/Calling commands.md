
# Index

- [[#Calling commands]]
	- [[#Checking return values]]
	- [[#Built-in commands vs external commands]]
- [[#Next Notes]]
# Calling commands

## Checking return values

Always check return values and give informative return values.

For unpiped commands, use $? or check directly via an __if__ statement to keep it simple.

Example:

```shell
if ! mv "${file_list[@]}" "${dest_dir}/"; then
  echo "Unable to move ${file_list[*]} to ${dest_dir}" >&2
  exit 1
fi

# Or
mv "${file_list[@]}" "${dest_dir}/"
if (( $? != 0 )); then
  echo "Unable to move ${file_list[*]} to ${dest_dir}" >&2
  exit 1
fi
```

Bash also has the PIPESTATUS variable that allows checking of the return code from all parts of a pipe. If it's only necessary to check success or failure of the whole pipe, then the following is acceptable:

```shell
tar -cf - ./* | ( cd "${dir}" && tar -xf - )
if (( PIPESTATUS[0] != 0 || PIPESTATUS[1] != 0 )); then
  echo "Unable to tar files to ${dir}" >&2
fi
```

However, as PIPESTATUS will be overwritten as soon as you do any other command, if you need to act differently on errors based on where it happened in the pipe, you'll need to assign PIPESTATUS to another variable immediately after running the command (don't forget that \[ is a command and will wipe out PIPESTATUS).

```shell
tar -cf - ./* | ( cd "${DIR}" && tar -xf - )
return_codes=( "${PIPESTATUS[@]}" )
if (( return_codes[0] != 0 )); then
  do_something
fi
if (( return_codes[1] != 0 )); then
  do_something_else
fi
```

## Built-in commands vs external commands

Give the choice between invoking a shell builtin and invoking a separate process, choose the builtin.

We prefer the use of builtins such as the __Parameter Expansion__ in bash (1) as it's more robust and portable (especially when compared to things like __sed__).

Examples:

```shell
# Prefer this:
addition=$(( X + Y ))
substitution="${string/#foo/bar}"

# Instead of this:
addition="$(expr "${X}" + "${Y}")"
substitution="$(echo "${string}" | sed -e 's/^foo/bar/')"
```

# Next Notes

[[AWK Overview]]