# Index

# Naming conventions

## Function names

Lower-case, with underscores to separate words. Separate libraries with : : . Parentheses are required after the function name. The keyword __function__ is optional, but must be used consistently throughout a project.

If you're writing single functions, use lowercase and separate words with underscore. If you're writing a package, separate package names with ::. Braces must be on the same line as the function name (as with other languages at Google) and no space between the function name and the parenthesis.

```shell
# Single function
my_func() {
  …
}

# Part of a package
mypackage::my_func() {
  …
}
```

The function keyword is extraneous when "()" is present after the function name, but enhances quick identification of functions.

## Variable names

As for function names.

Variables names for loops sould be similarly named for any variable you're looping through.

```shell
for zone in "${zones[@]}"; do
  something_with "${zone}"
done
```

## Constants and environment variable names

All caps, separated with underscores, declared at the top of the file.

Constants and anything exported to the environment should be capitalized.

```shell
# Constant
readonly PATH_TO_FILES='/some/path'

# Both constant and environment
declare -xr ORACLE_SID='PROD'
```

Some things become constant at their first setting (for example, via getopts). Thus, it's OK to set a constant in getopts or based on a condition, but it should be made readonly immediately afterwards. For the sake of clarity readonly or export is recommended instead of the equivalent declare commands.

```shell
VERBOSE='false'
while getopts 'v' flag; do
  case "${flag}" in
    v) VERBOSE='true' ;;
  esac
done
readonly VERBOSE
```

## Source filenames

Lowercase, with underscores to separate words if desired.

## Read-only variables

Use readonly or declare -r to ensure they're read only.

As globals are widely used in shell, it's important to catch error when working with them. When you declare a variable that is meant to be read-only, make this explicit.

```shell
zip_version="$(dpkg --status zip | grep Version: | cut -d ' ' -f 2)"
if [[ -z "${zip_version}" ]]; then
  error_message
else
  readonly zip_version
fi
```

## Use local variables

Declare function-specific variables with __local__. Declaration and assignment should be on different lines.

Ensure that local variables are only seen inside a function and its children by using __local__ when declaring them. This avoids polluting the global name space and inadvertently setting variables that may have significance outside the function.

Declaration and assignment must be separate statements when the assignment value is provided by a command substitution; as the __local__ builtin does not propagate the exit code from the command substitution.

```shell
my_func2() {
  local name="$1"

  # Separate lines for declaration and assignment:
  local my_var
  my_var="$(my_func)"
  (( $? == 0 )) || return

  …
}

my_func2() {
  # DO NOT do this:
  # $? will always be zero, as it contains the exit code of 'local', not my_func
  local my_var="$(my_func)"
  (( $? == 0 )) || return

  …
}
```

## Function location