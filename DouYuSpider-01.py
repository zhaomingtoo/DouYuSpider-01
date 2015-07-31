__author__ = 'Troll'
import urllib2
import re

class Spider():
    def __init__(self):
        self.url = "http://www.douyutv.com/directory/game/LOL"
        self.anchors = []
        self.rank_number = 1

    def get_page(self):
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
        temp_anchors = []
        anchors = re.findall(r'<span.*?class="nnt">(.*?)</span>', my_page, re.S)
        for anchor in anchors:
            temp_anchors.append(str(self.rank_number) + "." + anchor)
            self.rank_number += 1
        self.anchors.extend(temp_anchors)

    def start_spider(self):
        my_page = self.get_page()
        self.find_title(my_page)

if __name__ == "__main__":
    my_spider = Spider()
    my_spider.start_spider()
    for item in my_spider.anchors:
        print item
