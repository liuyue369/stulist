# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from dbconn1 import db_cursor

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("wangye/main.html")

class StudentListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("wangye/list.html", students = list_students())
def list_students():
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
class StudentCreateHandler(tornado.web.RequestHandler):
    def get(self):
        cou = dict(no='', name='', sex='', banji='',birthday='')
        self.render("wangye/create.html", student = cou)
    def post(self):
            no = self.get_argument("no")
            name = self.get_argument("name")
            birthday = self.get_argument("birthday")
            sex = self.get_argument("sex")
            banji = self.get_argument("banji")
            CreateStudent(no,name,birthday,sex,banji)
            self.redirect("/list")
            

def CreateStudent(no,name,birthday,sex,banji):
          with db_cursor() as cur : # 取得操作数据的游标，记为cur
           s="""
             INSERT INTO student (no, name, birthday, sex,banji) 
           VALUES(%(no)s, %(name)s, %(birthday)s, %(sex)s,%(banji)s)
             """
           cur.execute(s, dict(no=no, name=name, birthday=birthday,sex=sex,banji=banji,))



class StudentDropHandler(tornado.web.RequestHandler):
      def get(self):
        cou = dict(no='', name='', sex='', banji='',birthday='')
        self.render("wangye/drop.html", student = cou)
      def post(self):
            no = self.get_argument("no")
            name = self.get_argument("name")
            birthday = self.get_argument("birthday")
            sex = self.get_argument("sex")
            banji = self.get_argument("banji")
            dropStudent(no,name,birthday,sex,banji)
            self.redirect("/list")
def dropStudent(no,name,birthday,sex,banji):
          with db_cursor() as cur : # 取得操作数据的游标，记为cur
           s="""
             DELETE FROM student
             where no=%(no)s AND name=%(name)s AND birthday=%(birthday)s AND sex=%(sex)s AND banji=%(banji)s
             """
           cur.execute(s, dict(no=no, name=name, birthday=birthday,sex=sex,banji=banji,))






class StudentChangeHandler(tornado.web.RequestHandler):

       def get(self):
         cou = dict(no='', name='', sex='', banji='',birthday='',lastno='', lastname='', lastsex='', lastbanji='',lastbirthday='')
         self.render("wangye/change.html", student = cou)


       def post(self):
             no = self.get_argument("no")
             name = self.get_argument("name")
             birthday = self.get_argument("birthday")
             sex = self.get_argument("sex")
             banji = self.get_argument("banji")
             lastno = self.get_argument("lastno")
             lastname = self.get_argument("lastname")
             lastbirthday = self.get_argument("lastbirthday")
             lastsex = self.get_argument("lastsex")
             lastbanji = self.get_argument("lastbanji")
             changeStudent(no,name,birthday,sex,banji,lastno,lastname,lastbirthday,lastsex,lastbanji)
             self.redirect("/list")




def changeStudent(no,name,birthday,sex,banji,lastno,lastname,lastbirthday,lastsex,lastbanji):
          with db_cursor() as cur : # 取得操作数据的游标，记为cur
           s="""
             UPDATE student SET
             no=%(no)s,
             name=%(name)s,
             birthday=%(birthday)s,
             sex=%(sex)s,
             banji=%(banji)s
            where no=%(lastno)s AND name=%(lastname)s AND birthday=%(lastbirthday)s AND sex=%(lastsex)s AND banji=%(lastbanji)s
             """
           cur.execute(s, dict(no=no, name=name,birthday=birthday,sex=sex,banji=banji,lastno=lastno,lastname=lastname,lastbirthday=lastbirthday,lastsex=lastsex,lastbanji=lastbanji))                                   
             
             
            

    
       








        




         
         

        