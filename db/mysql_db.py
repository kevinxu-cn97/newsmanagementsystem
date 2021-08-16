# -*- encoding: utf-8 -*-
"""
@File    : mysql_db.py
@Time    : 2021-08-10 15:03
@Author  : XD
@Email   : gudianpai@qq.com
@Software: PyCharm
"""
#数据库连接池
import mysql.connector.pooling

#变量命名要严瑾，声明为私有变量
__config = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"xd19970306",
    "database":"vega",
}
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
except Exception as e:
    print(e)
