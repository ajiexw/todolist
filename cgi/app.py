#!/usr/bin/env python
#coding=utf-8

import web

urls = (
    '/','Index',        
)

render = web.template.render('page/')
db = web.database(dbn='mysql', user='todolist', pw='todolist_db_password', db='todolist')

class Index:
    def GET(self):
        projects = db.select('Project');
        todos = db.select('Item');
        return render.index(projects, todos)

app = web.application(urls,globals())

if __name__ == "__main__":
    app.run ()
