# -*- encoding: utf-8 -*-
"""
@File    : role_dao.py
@Time    : 2021-08-15 0:13
@Author  : XD
@Email   : gudianpai@qq.com
@Software: PyCharm
"""
from db.mysql_db import pool

class RoleDao:
    #查询角色列表
    def search_list(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT id,role FROM t_role"
            cursor.execute(sql)  # 只有一个参数参数用中括号去传
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()