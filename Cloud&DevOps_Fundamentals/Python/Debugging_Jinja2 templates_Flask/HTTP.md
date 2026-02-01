# Index

- [[#HTTP]]
	- [[#HTTP - Hypertext Transfer Protocol]]
	- [[#HTTP Requests]]
	- [[#HTTP URL]]
- [[#Next Notes]]
# HTTP

## HTTP - Hypertext Transfer Protocol

![[http.png]]

## HTTP Requests

![[http_requests.png]]

**GET** is used to request data from a specified resource.

**POST/PUT** is used to send data to a server to create/update a resource.

The difference between POST and PUT is that PUT requests are idempotent. That is, calling the same PUT request multiple times will always produce the same result. In contrast, calling a POST request repeatedly have the side effects of creating the same resource multiple times.

The **DELETE** method deletes the specified resource.

## HTTP URL

![[http_url.png]]

# Next Notes

[[Requests]]