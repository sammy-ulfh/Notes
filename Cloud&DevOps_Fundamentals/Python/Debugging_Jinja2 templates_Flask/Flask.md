# Index

- [[#Flask]]
- [[#Next Notes]]
# Flask

[https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

Flask is a lightweight framework.

The simple "Hello world" Flask application contains only 6 lines of code:

```python
# start.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

app.run()
```

So what did that code do?

- First we imported the Flask class. An instance of this class will be our WSGI application.
- Next we create an instance of this class. The first argument is the name of the application’s module or `package. __name__` is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
- We then use the `route()` decorator to tell Flask what URL should trigger our function.
- The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

To run the application:

```shell
$ pip install flask
$ python start.py
```

Then just open the URL: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

# Next Notes

[[HTTP]]

