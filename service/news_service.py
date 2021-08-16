# -*- encoding: utf-8 -*-
"""
@File    : news_service.py
@Time    : 2021-08-11 21:32
@Author  : XD
@Email   : gudianpai@qq.com
@Software: PyCharm
"""
from db.news_dao import NewDao

class NewsService:
    __news_dao = NewDao()

    # 查询待审批新闻的总页数
    # 查询待审批新闻列表
    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result

    # 查询待审批新闻的总页数
    def search_unreview_count_page(self):
        count_page = self.__news_dao.search_unreview_count_page()
        return count_page

    # 审批新闻
    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)

    # 查询新闻列表
    def search_list(self, page):
        count_page = self.__news_dao.search_list()

    # 查询新闻总页数
    def search_count_page(self):
        count_page = self.__news_dao.search_count_page()


    # 删除新闻
    def delete_by_id(self, id):
        self.__news_dao.delete_by_id(id)
