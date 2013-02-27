#!/usr/bin/env python
#coding=utf-8

import web

urls = (
    '/','Index',        
)

render = web.template.render('page/')

class Index:
    def GET(self):
        i = web.input()
        return render.index(i.name)

app = web.application(urls,globals())

if __name__ == "__main__":
    app.run ()
