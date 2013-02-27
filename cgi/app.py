#!/usr/bin/env python
#coding=utf-8

import web

urls = (
    '/','Index',        
)

class Index:
    def GET(self):
        return "Hello,todo"

app = web.application(urls,globals())

if __name__ == "__main__":
    app.run ()
