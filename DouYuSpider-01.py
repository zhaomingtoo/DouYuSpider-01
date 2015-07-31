# -*- coding:utf-8 -*-

"""
简单的python爬虫工具，用来爬取当前斗鱼LOL板块正在直播的前30名主播名称

Author= 'Troll'
Version:0.01
Date: 2015-7-31
Language:python 2.7.9
Editor: Pycharm
Operator: 请阅读README.md
"""

import urllib2
import re

class Spider():
    """类的简要说明

    本类主要用于抓取斗鱼LOL板块前30名主播的名称

    Attributes:
        url: 用于表示当前争取抓取页面的url
        anchors: 存储处理好的抓取到的主播名称
        rank_number: 用于显示排序
    """
    def __init__(self):
        self.url = "http://www.douyutv.com/directory/game/LOL"
        self.anchors = []
        self.rank_number = 1

    def get_page(self):
        """
        根据当前页码爬取网页HTML

        Returns:
            返回抓取到整个页面的HTML(unicode编码)

        Raises:
            URLError:url引发的异常
        """
        try:
            my_page = urllib2.urlopen(self.url).read().decode("utf-8")
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print "The server couldn't fulfill the request."
                print "Error code: %s" % e.code
            elif hasattr(e, "reason"):
                print "We failed to reach a server. Please check your url and read the Reason"
                print "Reason: %s" % e.reason
        return my_page

    def find_title(self, my_page):
        """

        通过返回的整个网页HTML, 正则匹配前100的电影名称

        Args:
            my_page: 传入页面的HTML文本用于正则匹配
        """
        temp_anchors = []
        anchors = re.findall(r'<span.*?class="nnt">(.*?)</span>', my_page, re.S)
        for anchor in anchors:
            temp_anchors.append(str(self.rank_number) + "." + anchor)
            self.rank_number += 1
        self.anchors.extend(temp_anchors)

    def start_spider(self):
        """

        爬虫入口

        """
        my_page = self.get_page()
        self.find_title(my_page)

if __name__ == "__main__":
    my_spider = Spider()
    my_spider.start_spider()
    for item in my_spider.anchors:
        print item
