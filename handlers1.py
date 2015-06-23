# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from dbconn import db_cursor

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/main.html")


class CourseListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/cou_list.html", students = dal_list_student())


def dal_list_student():
    data = []
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        SELECT  stu_no, name, birthday, sex, banji FROM student ORDER BY stu_sn DESC
        """
        cur.execute(s)      
        for r in cur.fetchall():
            stu = dict( stu_no=r[0], name=r[1], birthday=r[2], sex=r[3], banji=r[4])
            data.append(stu)
    print(data)
    return data

