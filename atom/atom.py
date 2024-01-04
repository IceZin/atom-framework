import sys
from flask import abort
from gevent import pywsgi, version_info, socket

from atom.handler import WebSocketHandler

b'''POST /login HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.33.0
Accept: */*
Cache-Control: no-cache
Postman-Token: 35aaa207-9586-411c-be38-cc4c27c576b8
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 148

{
    "username": "IceZin",
    "password": "$argon2id$v=19$m=65536,t=3,p=4$FH9rFHvU5MdiPGl5Z4KRfg$lwB1X8WfizKZDwX6S6u3QGsdLtoXjzmkz4Uek2RQMFI"
}'''

['POST', '/login', 'HTTP/1.1', 'Content-Type:', 'application/json', 'User-Agent:', 'PostmanRuntime/7.33.0',
 'Accept:', '*/*', 'Cache-Control:', 'no-cache', 'Postman-Token:', '03c15cc3-819e-4066-97c7-e4429e365c2f',
 'Host:', '127.0.0.1:5000', 'Accept-Encoding:', 'gzip,', 'deflate,', 'br', 'Connection:', 'keep-alive',
 'Content-Length:', '148', '{', '"username":', '"IceZin",',
 '"password":', '"$argon2id$v=19$m=65536,t=3,p=4$FH9rFHvU5MdiPGl5Z4KRfg$lwB1X8WfizKZDwX6S6u3QGsdLtoXjzmkz4Uek2RQMFI"', '}']


class Atom:
    def __init__(self, app):
        self.server = pywsgi.WSGIServer(("127.0.0.1", 5000), application=app, handler_class=WebSocketHandler)
        self.server.serve_forever()

    def apply(view):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(*args)
                print(**kwargs)

                view_result = view()
                print(view_result)

                if view_result:
                    return func(*args, **kwargs)
                else:
                    abort(401)
            return wrapper
        return decorator