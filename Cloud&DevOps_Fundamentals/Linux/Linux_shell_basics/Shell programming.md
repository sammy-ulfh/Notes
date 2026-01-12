# Index

- [[#Shell programming]]
  - [[#Environment variables and shell variables]]
  - [[#When not to user shell scripts]]
- [[#Next Notes]]

# Shell programming

SHELL is also a programming language:

- The syntax is simple and straightforward
- Most short scripts work right the first time
- Debugging is straightforward

The shell program interprets user commands, which are either directly entered by the user, or which can be read from a file called the shell script or shell program. Shell scripts are interpreted, not compiled. The shell reads commands from the script line per line and searches for those commands on the system, while a compiler converts a program into machine readable form, an executable file - which may then be used in a shell script.

## Environment variables and shell variables

In Linux and Unix based systems environment variables are a set of dynamic named values, stored within the system that are used by applications and shell scripts launched in shells or subshells. In simple words, an environment variable is a variable with a name and associated value.

Environment variables allow you to customize how the system works and the behavior of the applications on the system or use values of environment variables inside of your shell scripts. For example, the environment variable can store information about the default text editor or browser, the path to executable files, or the system locale and keyboard layout settings.

> Variables have the following format

> KEY=value
> ANOTHER_KEY="some other value"
> KEY_MULTI=value1:value2


- The __names__ of the variables are __case-sensitive__. By convention, environment variables should have UPPER_CASE name with underscored __\___ character netween words.
- When __assigning multiple values__ to the variable they must be __separated by the colon__ ==:== character.
- There is __no space around the equals__ ==\=== symbol.

Variables can be classified into to main categories, __environment variables__ and __shell variables__.

- __Environment variables__ are variables that are __available system-wide__ and are inherited by all spawned child processes and shells.
- __Shell variables__ are variables that __apply only to the current shell instance__. Each shell such as zsh and bash, has its own set of internal shell variables.

Command how to set environment and shell variables will be described in the next chapter.

Most of the common environment variables:

- __USER__: The current logged in user.
- __HOME__: The home directory of the current user.
- __EDITOR__: The default file editor to be used. This is the editor that will be used when you type edit in your terminal.
- __SHELL__: The path of the current user's shell, such as bash or zsh.
- __LOGNAME__: The name of the current user.
- __PATH__: A __list of directories to be searched when executing commands.__.
	  > When you run a command __the system will search those directories in this order and user the first found executable.
- __LANG__: The current locales settings.
- __TERM__: The current terminal emulation
- __MAIL__: Location of where the current user's mail is stored.

### When not to user shell scripts

- Resource-intensive tasks, specially where speed is a factor (sorting, hashing, recursion)
- Complex applications, where structured programming is a necessity (type-checking of variables, function prototypes, etc)
- Mission-critical applications upon which you are betting the future of the company
- Simulations where security is important, where you need to guarantee the integrity of your system and protect against intrusion, cracking, and vandalism
- Need native support for multi-dimensional arrays
- Need data structures, such as linked list or trees
- Need to generate / manipulate graphics or GUIs
- Need to use libraries or interface with legacy code
- Proprietary, closed-source applications (Shell scripts put the source code right out in the open for all the world to see)

# Next Notes

[[Basic shell commands]]