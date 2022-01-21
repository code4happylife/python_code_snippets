# encoding: utf-8
'''
@author: developer
@software: python
@file: test_wsgi.py
@time: 2022/1/21 21:47
@desc:
'''
from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults


def simple_app(environ, start_response):
    setup_testing_defaults(environ)
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    url = environ["PATH_INFO"]
    if url == '/index':
        response = '<h1>这里是Index 页面</h1>'
    elif url == '/detail':
        response = '<h1>这里是Detail 页面</h1>'
    elif url == '/drink/':
        response = '<h1>这里是Drink 页面</h1>'
    else:
        response = '<h1 style="color:red;">这里是 404 页面</h1>'
    return [response.encode('utf-8')]


if __name__ == '__main__':
    httpd = make_server('', 8000, simple_app)
    httpd.serve_forever()

    '''
    127.0.0.1 - - [21/Jan/2022 22:25:56] "GET /drink/ HTTP/1.1" 200 30
127.0.0.1 - - [21/Jan/2022 22:25:56] "GET /favicon.ico HTTP/1.1" 200 48
    '''
