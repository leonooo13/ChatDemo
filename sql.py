import sqlite3
def createtble():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # 创建 user 表
    sql_createtable='''CREATE TABLE
     user( 
         user_id int,
         user_name text,
         password text 
         )'''
    c.execute(sql_createtable)
    conn.close()
def inserttable(sql):
    conn=sqlite3.connect('example.db')
    # 插入数据
    sql_insert="INSERT INTO user(user_id, user_name, password) VALUES (1, 'admin', 'admin')"
    c=conn.cursor()
    c.execute(sql_insert)
    conn.commit()
    conn.close()
# 查询数据
def select(sql:str,parm:tuple):
    conn=sqlite3.connect('example.db')
    c=conn.cursor()
    c.execute(sql,parm)
    result = c.fetchone()
    conn.close()
    return result