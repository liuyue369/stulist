#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn1 import db_cursor

def chuangjianbiao():
    sqlstr = """
    DROP TABLE IF EXISTS student;
    CREATE TABLE IF NOT EXISTS student  (
         no       VARCHAR(10), --学号 
         name     TEXT,        --姓名
         birthday TEXT,        --出生时间
         sex      VARCHAR(10),   --性别
         banji    TEXT         --班级
        
     );
"""
    
    with db_cursor() as cur :
        cur.execute(sqlstr)
def charushuju():
    sqlstr = """
    DELETE FROM student ;
    INSERT INTO student (no, name, birthday,sex,banji)  VALUES
    (123456,'张三','2015-01-20','男','1301');
    """
    with db_cursor() as cur :
        cur.execute(sqlstr) 
if __name__ == '__main__':
     chuangjianbiao()
     charushuju ()
     print('数据库已初始化完毕！')

    
        
    

