
import os
from webob import Response
from webob.dec import wsgify
from webob import exc
from paste import httpserver
from paste.deploy import loadapp





path_str = os.getcwd()
INI_PATH = path_str + '/webopaste.ini'

@wsgify
def application(request):
    return Response('Hello World of WebOb!')

@wsgify.middleware
def auth_filter(request, app):
    #if request.headers.get('X-Auth-Token') != 'somestring':
    #    return exc.HTTPForbidden()
    return app(request)

def app_factory(global_config, **local_config):
    return application

def filter_factory(global_config, **local_config):
    return auth_filter

wsgi_app = loadapp('config:' + INI_PATH)



httpserver.serve(wsgi_app, host='127.0.0.1', port=8080)