#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor

def create_db():
    sqlstr = """
    DROP TABLE IF EXISTS student;

    CREATE TABLE IF NOT EXISTS student  (
        stu_sn   INTEGER,     --序号
        stu_no   TEXT,        --学号
        name     TEXT,        --姓名
        sex      TEXT,        --性别
        birthday    DATE,     --出生日期
        banji    TEXT,         --班级
        PRIMARY KEY(stu_sn)
    );
    -- CREATE UNIQUE INDEX idx_student_no ON student(stu_no);

    CREATE SEQUENCE seq_stu_sn 
        START 10000 INCREMENT 1 OWNED BY student.stu_sn;

    """
    with db_cursor() as cur :
        cur.execute(sqlstr) # 执行SQL语句
    
def init_data():
    sqlstr = """
    DELETE FROM student;

    INSERT INTO student (stu_sn, stu_no, name, sex, birthday, banji)  VALUES 
        (01, '1310650101',  '琪琪', '男', '1995/06/05', '信息1301'), 
        (02, '1310650102',  '刘芳', '女', '1994/09/12', '信息1302'),
        (03, '1310650128',  '李丽', '女', '1996/06/03', '信息1304');

    """
    with db_cursor() as cur :
        cur.execute(sqlstr)    

if __name__ == '__main__':
    create_db()
    init_data()
    print('数据库已初始化完毕！')

