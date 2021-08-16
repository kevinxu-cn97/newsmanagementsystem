# -*- encoding: utf-8 -*-
"""
@File    : role_service.py
@Time    : 2021-08-15 0:15
@Author  : XD
@Email   : gudianpai@qq.com
@Software: PyCharm
"""
from db.role_dao import RoleDao

class RoleService:
    __role_dao = RoleDao()

    #查询角色列表
    def search_list(self):
        result = self.__role_dao.search_list()
        return result