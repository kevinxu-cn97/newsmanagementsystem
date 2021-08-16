# -*- encoding: utf-8 -*-
"""
@File    : user_dao.py
@Time    : 2021-08-11 0:03
@Author  : XD
@Email   : gudianpai@qq.com
@Software: PyCharm
"""
from db.mysql_db import pool
# data access object
class UserDao:
    #验证用户登录
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user WHERE username = %s AND " \
                  "AES_DECRYPT(UNHEX(password),'HELLO WORLD')=%s"
            cursor.execute(sql,(username, password))
            count = cursor.fetchone()[0]
            con.close()
            return True if count==1 else False
        except Exception as e:
            print(e)

    def search_user_role(self, username):
        """
        查询用户角色
        :param username:
        :return:
        """

        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT r.role FROM t_user u JOIN t_role r ON u.role_id=r.id " \
                  "WHERE u.username=%s"
            cursor.execute(sql, [username])#只有一个参数参数用中括号去传
            role = cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    def delete_by_id(self, id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "DELETE FROM t_user WHERE id=%s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if con in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

        # 添加记录

    def insert(self, username, password, email, role_id):
        try:
            #HEX避免乱码
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "INSERT INTO t_user(username,password,email,role_id) " \
                  "VALUES(%s,HEX(AES_ENCRYPT(%s,'HelloWorld')),%s,%s)"
            cursor.execute(sql, (username, password, email, role_id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()

    #查询用户总页数
    def search_count_page(self):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*)/10 FROM t_user"
            cursor.execute(sql)#只有一个参数参数用中括号去传
            count_page = cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()

    # 查询用户分页记录
    def search_list(self, page):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT u.id,u.username,r.role " \
                  "FROM t_user u JOIN t_role r " \
                  "ON u.role_id=r.id " \
                  "ORDER BY u.id " \
                  "LIMIT %s,%s"
            cursor.execute(sql, ((page - 1) * 10, 10))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if "con" in dir():
                con.close()
    #修改用户
    def update(self, id, username, password, email, role_id):
        try:
            con = pool.get_connection()
            con.start_transaction()
            cursor = con.cursor()
            sql = "UPDATE t_user SET username=%s," \
                  "password=HEX(AES_ENCRYPT(%s,'HelloWorld'))," \
                  "email=%s,role_id=%s " \
                  "WHERE id=%s"
            cursor.execute(sql, (username, password, email, role_id, id))
            con.commit()
        except Exception as e:
            if "con" in dir():
                con.rollback()
            print(e)
        finally:
            if "con" in dir():
                con.close()