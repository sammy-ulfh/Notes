# Index

- [[#PIP]]
- [[#Environment snapshot]]
- [[#Next Notes]]

# PIP

[pip](http://pip-installer.org/) is a tool for installing Python packages from the [Python Package Index](http://pypi.python.org/) (PyPI)

Install package:

```shell
pip install <package_name>
```

Upgrade already installed package:

```shell
pip install --upgrade <package_name>
```

Install package of a particular version:

```shell
pip install <package_name>=='version_num'
```

Install the version that satisfies the criteria:

```shell
pip install <package_name> >= 'version_num'
```

Upgrade pip:

```shell
pip install -U pip
```

Search package

```shell
pip search "query"
```

## Environment snapshot

Generate a requirements file:

```shell
pip freeze > requirements.txt
```

Install from it in another environment:

```shell
pip install -r requirements.txt
```

Packages are listed in a case-insensitive sorted order:

```shell
$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

# Next Notes

[[Scripts]]


