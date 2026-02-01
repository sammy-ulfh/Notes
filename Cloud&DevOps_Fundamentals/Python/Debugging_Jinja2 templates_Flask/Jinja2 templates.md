# Index

- [[#Jinja2 templates]]
	- [[#Configuration file]]
	- [[#Installation]]
	- [[#Basic Example]]
	- [[#Using yaml]]
	- [[#Variables]]
	- [[#IF]]
	- [[#FOR]]
- [[#Next Notes]]
# Jinja2 templates

## Configuration file

**Jinja2** is a powerful and easy-to-use python-based templating engine that comes in handy in an IT environment with multiple servers where configurations vary every other time. Creating static configuration files for each of these nodes is tedious and may not be a viable option since it will consume more time and energy. And this is where templating comes in.

Let's demonstrate Jinja2 usage by example. We have an Apache configuration that we should customize for different environments:

```j2
NameVirtualHost *:80

<VirtualHost *:80>
  ServerName www.domain.tld
  DocumentRoot /www/domain
  ServerAdmin www-admin@foo.example.com
  <Directory "/usr/local/httpd/htdocs">
     AllowOverride All
     Options Indexes FollowSymLinks
     Order allow,deny
     Allow from all
  </Directory>
</VirtualHost>
```

Save this configuration in `vhosts.j2` file

## Installation

Install Jinja2 and PyYAML before proceeding further:

```shell
pip install Jinja2
pip install pyyaml
```

## Basic Example

A Jinja2 template file is a text file that contains variables that get evaluated and replaced by actual values upon runtime or code execution. In a Jinja2 template file, you will find the following tags:

`{{ }}`  : These double curly braces are the widely used tags in a template file and they are used for embedding variables and ultimately printing their value during code execution. For example, a simple syntax using the double curly braces is as shown: The {{ webserver }} is running on  {{ nginx-version }}

`{%  %}` : These are mostly used for control statements such as loops and if-else statements.

`{#  #}` : These denote comments that describe a task.

Hello world example:

```python
from jinja2 import Template

template = Template('Hello {{ name }}!')
message = template.render(name='John Doe')

print(message)  # 'Hello John Doe!'
```

## Using yaml

We will use yaml-file to store values. The following script renders the template with provided values.

```python
import yaml
from jinja2 import Template

with open('data.yml') as data_file:
    config_data = yaml.load(data_file, Loader=yaml.FullLoader)

with open('vhosts.j2') as template_file:
    template_html = template_file.read()

template = Template(template_html)
vhosts_conf = template.render(config_data)

with open('vhosts.conf', 'w') as vhosts_file:
    vhosts_file.write(vhosts_conf)
```

## Variables

Let's update `vhosts.j2` created before. Our first step is to replace the following values with `{{ }}` variables. The values should be moved to `data.yaml:`

```
{{ servername }}

{{ documentroot }}

{{ serveradmin }}

{{ directorypath }}
```

__data.yml__

```yml
servername: …
documentroot: …
...
```

It is time to verify updates and run rendering apache configuration from the template:

```shell
$ python conf.py
```

## IF

The next step is to add if-statement. Let's check whether `serveradmin` is defined. If not, `ServerAdmin` section won't be added to apache configuration:

```
{% if serveradmin %}
  ServerAdmin {{ serveradmin }}
{% endif %}
```

To test your updates in `vhosts.j2`, temporarily remove `serveradmin` value from `data.yaml` and run `conf.py`.

## FOR

The next structure that should be added is for-loop. In order to be able to add several `VirtualHost` sections to the apache configuration, surround `VirtualHost` section with `for`-statement:

```
{% for vhost in apache_vhosts %}
    <VirtualHost *:80>
        ServerName {{ vhost.servername }}
        …
    </VirtualHost>
{% endfor %}
```

__data.yml__

`data.yaml` file should be updated accordingly:

```
apache_vhosts:
- servername: …
 documentroot: …
       …
- servername: …
  documentroot: …
       …
```

Test your changes:

`$ python conf.py`

# Next Notes
