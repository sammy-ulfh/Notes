# Index

- [[#Debugging]]
	- [[#Debugging in python]]
	- [[#Logging]]
	- [[#syslog]]
	- [[#Logging]]
- [[#Next Notes]]
# Debugging

## Debugging in python

In order to debug an error in Python, we can use debuggers and, in addition, add logging to the application.

![[debugging_in_python.png]]

## Logging

Logging is a very useful tool in a programmer’s toolbox. It can help you develop a better understanding of the flow of a program and discover scenarios that you might not even have thought of while developing.

Logs provide developers with an extra set of eyes that are constantly looking at the flow that an application is going through. They can store information, like which user or IP accessed the application. If an error occurs, then they can provide more insights than a stack trace by telling you what the state of the program was before it arrived at the line of code where the error occurred.

By logging useful data from the right places, you can not only debug errors easily but also use the data to analyze the performance of the application to plan for scaling or look at usage patterns to plan for marketing.

Python provides a logging system as a part of its standard library, so you can quickly add logging to your application. In this article, you will learn why using this module is the best way to add logging to your application as well as how to get started quickly, and you will get an introduction to some of the advanced features available.

![[logging.png]]

## syslog

```python
#debug.py
from syslog import syslog
syslog('This is a debug message.')
```

```python
$ python debug.py
$ tail /var/log/syslog # This
$ journalctl -t python -e # Or this
```

## Logging

The [logging module](https://docs.python.org/3/library/logging.html) in Python is a ready-to-use and powerful module that is designed to meet the needs of beginners as well as enterprise teams. It is used by most third-party Python libraries, so you can integrate your log messages with the ones from those libraries to produce a homogeneous log for your application.

logging supports different levels of errors:

```python
import logging  
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

Examples of logging messages:

```txt
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```

You can specify the level of logging. In this case, only messages of defined level and higher are output:

```python
import logging  
logging.basicConfig(level=logging.INFO)
logging.info('This will get logged')  
logging.debug('This will not get logged')
```

The output format can be customized:

```python
import logging

logging.basicConfig(filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')
logging.error('This will get logged to a file')

# root - ERROR - This will get logged to a file
```

Complex configuration can be provided in a configuration file. Here is an example of a configuration file and its loading in python code:

```yaml
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
  file:
    class : logging.handlers.RotatingFileHandler
    formatter: precise
    filename: logconfig.log
    maxBytes: 1024
    backupCount: 3
loggers:
  simpleExample:
    level: DEBUG
    handlers: [console]
    propagate: no
root:
  level: DEBUG
  handlers: [console]
```

```python
import logging
import logging.config
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("simpleExample")

logger.debug('This is a debug message')
```

# Next Notes

[[PDB]]