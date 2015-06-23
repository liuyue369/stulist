# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("wangye/1.html")
        
class StudentListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("wangye/2.html", students = list_students())

def list_courses():
    data = []
    with db_cursor() as cur : 
        s = """
        SELECT no, name, birthday, sex ,banji FROM student ORDER BY banji
        """
        cur.execute(s)      
        for r in cur.fetchall():
            cou = dict(no=r[0], name=r[1], birthday=r[2], sex=r[3],banji=r[4])
            data.append(cou)
    return data
class CourseCreateHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("wangye/3.html", students = stu)
    def post(self, banji):
        no = self.get_argument('no')
        name = self.get_argument('name', '')
        birthday = self.get_argument('birthday', '')
        sex = self.get_argument('sex', '')
        banji = self.get_argument('banji', '')
    
        
      
