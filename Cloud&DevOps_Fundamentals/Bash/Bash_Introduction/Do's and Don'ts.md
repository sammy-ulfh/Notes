
# Index

- [[#Do's and Don'ts]]
	-   [[#Shell should not be used for]]
- [[#Next Notes]]

# Do's and Don'ts

Shell __should__ only be used for small utilities or simple wrapper scripts.

While shell scripting isn't a development language, it is used for writing various utility scripts throughout Google, This style guide is more a recognition of its use rather than a suggestion that it be used for widespread deployment.

Some guidelines:

- If you're mostly calling other utilities and are doing relatively little data manipulation, shell is an acceptable choice for the task.
- If performance matters, use something other than shell.
- If you are writing a script that is more than 100 lines long, or that uses non-straightforward control flow logic, you should rewrite it in a more structured language now. Bear in mind that scripts grow. Rewrite your script early avoid a more time-consuming rewrite at later date.
- When assessing the complexity of your code (e.g. to decide whether to switch language) consider whether the code is easily maintainable by people other that its author.

## Shell should not be used for

- Resource-intensive tasks, specially where a speed is a factor (storing, hashing, recursion)
- Complex application, where structured programming is a necessity (type-checking of variables, function prototypes, etc.)
- Mission-critical applications upon which you are betting the future of the company
- Situations where security is important, where you need to guarantee the integrity of your system and protect against intrusion, cracking, and vandalism
- Need native support for multi-dimensional arrays
- Need data structured, such as linked list or trees
- Need to generate / manipulate graphics or GUIs
- Need to use libraries or interface with legacy code
- Proprietary, closed-source applications (Shell scripts put the source code right out in the open for all the world to see.)

# Next Notes

[[Script Development and Invocation]]