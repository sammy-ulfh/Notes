# Index

- [[#Packaging]]
	- [[#Package Directory Structure]]
	- [[#setup.py]]
	- [[#Create package]]
	- [[#Create package Example]]
	- [[#Install package Example]]
- [[#Next Notes]]
# Packaging

## Package Directory Structure

The project should be structured properly before creating an installation package. Let's demonstrate it in an example (the project is [attached](https://elearn.epam.com/asset-v1:RD_CIS+DOBCPython+0422+type@asset+block@zoo-example.zip)).

```
zoo-example
├── animals
│   ├──handlers
│   │  ├── __init__.py
│   │  ├── walk.py
│   │  └── swim.py
│   ├── __init__.py
│   ├── crocodile.py
│   ├── monkey.py
│   └── zoo.py
├── README.md
└── setup.py
```

- all code is moved to a separate directory: animals
- README.md file with project description is added
- setup.py is created

## setup.py

The setup script is the centre of all activity in building, distributing, and installing modules using the Distutils. The main purpose of the setup script is to describe your module distribution to the Distutils, so that the various commands that operate on your modules do the right thing.

```python
from setuptools import setup, find_packages
setup(
    # name of package
    name="zoo-example", 
    # packages (directories) to be included
    packages=find_packages(),
    # script entry point
    entry_points={
        "console_scripts": [
            "zoo = animals.zoo:main",
        ],
    },
    # package dependencies
    install_requires=[
        "termcolor==1.1.0",
    ],
    version="0.1",
    author="Captain Jack",
    author_email="captain_jack@gmail.com",
    description="Example of the test application",
    license="MIT")
```

**Entry points** are a type of metadata that can be exposed by packages on installation. They are a very useful feature of the Python ecosystem, and come especially handy when the package would like to provide commands to be run at the terminal. This functionality is known as console scripts.

```shell
$ zoo
Welcome to the zoo!
```

When a user enters `**zoo**` command, `**main()**` function from `**zoo.py**` (located in **`animal`** folder) is invoked.

`find_packages()` returns a list all Python packages found within directory.

## Create package

__Create egg__

```shell
$ python setup.py bdist_egg
```

__Create wheel (pip install wheel)___

```shell
$ python setup.py bdist_wheel
```

__Help commands__

```shell
$ python setup.py --help-commands
```

__Universal wheel__

```shell
$ python setup.py bdist_wheel --universal
```

__Source archive__

```shell
$ python setup.py sdist
```

## Create package: Example

```shell
$ pip install wheel
$ python setup.py bdist_wheel
```

We can find new directories after command execution. `dist` contains distributives. `*.egg-info` stores information about files and packages added to distributive.

```
zoo-example
...
├── dist
│   └── zoo_example-0.1-py3-none-any.whl
└── zoo_example.egg-info
    ├── dependency_links.txt
    ├── PKG-INFO
    ├── SOURCES.txt
    └── top_level.txt
```

__Install packages__

```shell
$ pip install <package_name>
```

__Upgrade already installed package__

```shell
$ pip install --upgrade <package_name>
```

__Install package of particular version__

```shell
$ pip install <package_name>=='version_num'
```

__Install version that satisfy a criteria__

```shell
$ pip install <package_name> >= 'version_num'
```

__Upgrading pip__

```shell
$ pip install -U pip
```

__Search package__

```python
$ pip search "query"
```

## Install package: Example

```shell
$ pip install .
```

or

```shell
$ pip install /home/user/zoo-example
```

or

```shell
$ pip install dist/zoo_example-0.1-py3-none-any.whl
```

```shell
$ python
>>> import animals
>>> animals.__path__
['/home/user/.pyenv/versions/devops/lib/python3.7/site-packages/animals']
```

```shell
$ pip uninstall zoo-example
```

# Next Notes