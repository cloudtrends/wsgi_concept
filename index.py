#!/usr/bin/env python


"""
Web Server Gateway Interface (WSGI)

https://docs.python.org/2/library/wsgiref.html


wsgiref is a reference implementation of the WSGI specification that can be used to add WSGI support to a web server or framework.



"""

from wsgiref.validate import validator

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

def application(environ, start_response):
    setup_testing_defaults(environ)

    # Sorting and stringifying the environment key, value pairs
    response_body = ['%s: %s' % (key, value)   for key, value in sorted(environ.items())]
    response_body = '\n'.join(response_body)
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]


# This is the application wrapped in a validator
validator_app = validator(application)


# Instantiate the WSGI server.
# It will receive the request, pass it to the application
# and send the application's response to the client
httpd = make_server(
       'localhost', # The host name.
       8051, # A port number where to wait for the request.
       validator_app # Our application object name, in this case a function.
       )
httpd.serve_forever()


