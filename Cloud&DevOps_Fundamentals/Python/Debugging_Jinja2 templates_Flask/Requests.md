# Index

- [[#Requests]]
	- [[#Requests - response]]
	- [[#Requests - Authentication]]
	- [[#Requests - Parameters]]
	- [[#Requests - JSON]]
	- [[#URLIB]]
- [[#Next Notes]]
# Requests

[https://requests.readthedocs.io/](https://requests.readthedocs.io/)

**Requests** is a simple, yet elegant, HTTP library. Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the JSON method.

Requests is one of the most downloaded Python packages today, pulling in around 30M downloads/week— according to GitHub, Requests is currently depended upon by 1,000,000+ repositories. You may certainly put your trust in this code.

```shell
$ pip install requests
```

```python
import requests

response = requests.get('https://api.github.com')

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

if response:
    print('Success!')
else:
    print('An error has occurred.')
```

## Requests - response

```python
>>> response = requests.get('https://api.github.com')
>>> response.content
b'{"current_user_url":"https://api.github.com/user",...}'

>>> response.text
'{"current_user_url":"https://api.github.com/user",...}'

>>> response.json()
{'current_user_url': 'https://api.github.com/user', }
```

## Requests - Authentication

```python
requests.get('https://api.github.com/user', auth=('user', 'pass'))


requests.get('https://git.epam.com/api/v4/projects',
             headers={'Authorization': Bearer myToken'})
```

## Requests - Parameters

```python
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('https://some.org/obj', params=payload)
>>> print(r.url)

https://some.org/obj?key2=value2&key1=value1
```

## Requests - JSON

```python
j = [{"name": "cat", "items": [{"num": 1, "price": 30}, {"num": 2, "price": 50}]}]

How to get num = 2 price?
result = j[0][“items”][1][“price”]
```

## URLIB

`https://docs.python.org/3/howto/urllib2.html`

![[urlib.png]]

## Next Notes

[[Testing]]