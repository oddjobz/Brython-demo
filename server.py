#!/usr/bin/env python

from sanic import Sanic

app = Sanic()
app.static('/', '.')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)