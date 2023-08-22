# Python Requests Module
'''
Syntax
requests.methodname(params)

Methods

Method	Description

delete(url, args)	-> Sends a DELETE request to the specified url

get(url, params, args)-> Sends a GET request to the specified url

head(url, args)	-> Sends a HEAD request to the specified url

patch(url, data, args) ->	Sends a PATCH request to the specified url

post(url, data, json, args) ->	Sends a POST request to the specified url

put(url, data, args) -> Sends a PUT request to the specified url

request(method, url, args) ->	Sends a request of the specified method to the specified url
'''
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)