# Index

- [[#Virtual environments]]
	- [[#Installation]]
	- [[#Create a virtual environment for a specified version of Python]]
	- [[#Activate/Deactivate/Unistall virtualenv]]
	- [[#Example]]
	- [[#Pyenv directory structure]]
- [[#Next Notes]]
# Virtual environments

Every beginning software developer has experienced, how frustrating it can be to use several versions of python on one computer.

![[pythonenv.png]]

If you wish to use multiple versions of Python on a single machine, then a virtual environment tool should be used to switch between python versions.

Popular virtual environment tools:

- virtualenv
- pyenv
- pipenv
- python -m -venv

A __virtual environment__ is a Python environment such that the Python interpreter, libraries, and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system.

A virtual environment is a directory tree that contains Python executable files and other files which indicate that it is a virtual environment.

Common installation tools such as **setuptools** and **pip** work as expected with virtual environments. In other words, when a virtual environment is active, they install Python packages into the virtual environment without needing to be told to do so explicitly.

We will use **pyenv** in our course.

## Installation

Find more information about the installation and the tool here: `https://github.com/yyuu/pyenv`

Install:

```shell
curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

List of all available Python versions:

```shell
pyenv install -l
```

Install a python version:

```shell
pyenv install <version>
```

List installed versions:

```shell
pyenv versions
```

Set python global version:

```shell
pyenv global <version>
```

## Create a virtual environment for a specified version of Python

```shell
pyenv virtualenv <version> <venv_name>
```

For instance:

```shell
pyenv virtualenv 3.9.6 my-project
```

## Activate/Deactivate/Unistall virtualenv

```shell
$ pyenv activate <venv_name>
$ pyenv deactivate
$ pyenv uninstall <venv_name>
```

## Example

```shell
$ pyenv install 3.8.11
$ pyenv global 3.8.11
$ pyenv virtualenv flaskage
$ pyenv local flaskage
$ pip install requests
$ pip freeze
```

`pyenv local <version>` -- automatically select Python version or virtual environment whenever you are in the current directory (or its subdirectories)

## Pyenv directory structure

![[pyenvstructureddir.png]]

Each python version has its own **python** and **pip** executables. Each python environment has its own **site-packages** folder where libraries are installed.
# Next Notes

[[PIP]]