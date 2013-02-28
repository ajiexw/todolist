#!/usr/bin/env python
#coding=utf-8

import web

urls = (
    '/','Index',
    '/add-project','AddProject', #添加项目
    '/add-item','AddItem', #添加任务
    '/del-item/(\d*)','DelItem', #删除任务
    '/finish-item/(\d*)','FinishItem', #任务完成
    '/unfinish-item/(\d*)','UnFinishItem', #返工任务
)

render = web.template.render('page/')
db = web.database(dbn='mysql', user='todolist', pw='todolist_db_password', db='todolist')

class Index:
    def GET(self):
        projects = db.select('Project');
        todos = db.select('Item', where="done=0");
        finish_todos = db.select('Item', where="done=1");
        return render.index(projects, todos, finish_todos)

class AddProject:
    def POST(self):
        i = web.input()
        new_id = db.insert('Project',title=i.title)
        raise web.seeother('/')

class AddItem:
    def POST(self):
        i = web.input()
        new_id = db.insert('Item',content=i.content)
        raise web.seeother('/')

class DelItem:
    def GET(self,item_id):
        item_id = int(item_id)
        db.delete('Item', where="Itemid=%s"%(item_id))
        raise web.seeother('/')

class FinishItem:
    def GET(self,item_id):
        item_id = int(item_id)
        db.update('Item', where="Itemid=%s"%(item_id), done=1)
        raise web.seeother('/')

class UnFinishItem:
    def GET(self,item_id):
        item_id = int(item_id)
        db.update('Item', where="Itemid=%s"%(item_id), done=0)
        raise web.seeother('/')
    
app = web.application(urls,globals())

if __name__ == "__main__":
    app.run ()
