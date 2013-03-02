#!/usr/bin/env python
#coding=utf-8

import web

urls = (
    '/','Index',
    '/(\d*)','Project',
    '/add-project','AddProject', #添加项目
    '/del-project/(\d*)','DelProject', #删除项目
    '/add-item','AddItem', #添加任务
    '/update-item/(\d*)','UpdateItem', #修改任务
    '/del-item/(\d*)','DelItem', #删除任务
    '/finish-item/(\d*)','FinishItem', #任务完成
    '/unfinish-item/(\d*)','UnFinishItem', #返工任务
)

render = web.template.render('page/')
db = web.database(dbn='mysql', user='todolist', pw='todolist_db_password', db='todolist')

class Index:
    def GET(self):
        web.seeother('/1')

class Project:
    def GET(self,project_id):
        project_id = int(project_id)
        projects = db.select('Project');
        project = db.select('Project', where="Projectid=%s"%(project_id))[0]
        todos = db.select('Item', where="done=0 and Projectid=%s"%(project_id))
        finish_todos = db.select('Item', where="done=1 and Projectid=%s"%(project_id))
        return render.index(projects, project, todos, finish_todos)

class AddProject:
    def POST(self):
        i = web.input()
        new_id = db.insert('Project',title=i.title)
        raise web.seeother('/')

class DelProject:
    def GET(self,project_id):
        project_id = int(project_id)
        db.delete('Project', where="Projectid=%s"%(project_id))
        raise web.seeother('/')

class AddItem:
    def POST(self):
        i = web.input()
        new_id = db.insert('Item',Projectid=i.Projectid, content=i.content)
        raise web.seeother('/')

class UpdateItem:
    def POST(self, item_id):
        i = web.input()
        new_id = db.update('Item', where="Itemid=%s"%(item_id), content=i.content)
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
