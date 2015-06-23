# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from dbconn import db_cursor

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/main.html")


class StudentListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/stu_list.html", students = dal_list_students())

class StudentEditHandler(tornado.web.RequestHandler):
    def get(self, stu_sn):

        stu = None
        if stu_sn != 'new' :
            stu = dal_get_student(stu_sn)
        
        if stu is None:
            stu = dict(stu_sn='new', stu_no='', name='', sex='', birthday='', banji='')

        self.render("pages/stu_edit.html", student = stu)

    def post(self, stu_sn):
        stu_no = self.get_argument('stu_no')
        name = self.get_argument('name', '')
        sex = self.get_argument('sex', '')
        birthday = self.get_argument('birthday', '')
        banji = self.get_argument('banji', '')

        if stu_sn == 'new' :
            dal_create_student(stu_no, name, sex, birthday, banji)
        else:
            dal_update_student(stu_no, name, sex, birthday, banji)

        self.redirect('/stulist')

class StudentDelHandler(tornado.web.RequestHandler):
    def get(self, stu_sn):
        dal_del_student(stu_sn)
        self.redirect('/stulist')

# -------------------------------------------------------------------------

def dal_list_students():
    data = []
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        SELECT stu_no, name, sex, birthday, banji FROM student ORDER BY stu_sn DESC
        """
        cur.execute(s)      
        for r in cur.fetchall():
            stu = dict(stu_sn=r[0], stu_no=r[1], name=r[2], sex=r[2], birthday=r[3], banji=r[3])
            data.append(stu)
    return data


def dal_get_student(stu_sn):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        SELECT stu_sn, stu_no, name, sex, birthday, banji  FROM student WHERE stu_sn=%s
        """
        cur.execute(s, (stu_sn, ))
        r = cur.fetchone()
        if r :
            return dict(stu_sn=r[0], stu_no=r[1], name=r[2], sex=r[2], birthday=r[3], banji=r[3])


def dal_create_student(stu_no, name, sex, birthday, banji):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        cur.execute("SELECT nextval('seq_stu_sn')")
        stu_sn = cur.fetchone()
        assert stu_sn is not None

        print('新课程内部序号%d: ' % stu_sn)

        s = """
        INSERT INTO student (stu_sn, stu_no, name, sex, birthday, banji) 
        VALUES (%(stu_sn)s, %(stu_no)s, %(name)s, %(sex)s, %(birthday)s, %(banji)s)
        """
        cur.execute(s, dict(stu_sn=stu_sn, stu_no=stu_no, name=name, sex=sex, birthday=birthday, banji=banji))


def dal_update_student(stu_sn, stu_no, name, sex, birthday, banji):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        UPDATE student SET
          stu_no=%(stu_no)s, 
          name=%(name)s, 
          sex=%(sex)s,
          birthday=%(birthday)s,
          banji=%(banji)s
        WHERE stu_sn=%(stu_sn)s
        """
        cur.execute(s, dict(stu_sn=stu_sn, stu_no=stu_no, name=name, sex=sex, birthday=birthday, banji=banji))


def dal_del_student(stu_sn):
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        DELETE FROM student WHERE stu_sn=%(stu_sn)s
        """
        cur.execute(s, dict(stu_sn=stu_sn))
        print('删除%d条记录' % cur.rowcount)
