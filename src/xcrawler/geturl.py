from HTMLParser import HTMLParser
import urllib
import sys
class parselinks(HTMLParser):
    def __init__(self):
        self.data=[]
        self.links = []
        self.href=0
        self.linkname=''
        HTMLParser.__init__(self)

    def handle_starttag(self,tag,attrs):
        if tag =='a':
            for name,value in attrs:
                if name == 'href':
                    self.href=1
                    if 'http' in value:
                        self.links.append(value.strip())

    def saveurl(self,r):
        for value in self.links:
            r.lpush('urllist',value)
            print "url"


if __name__=="__main__":
    IParser = parselinks()
    IParset.feed(urllib.urlopen("http://www.sina.com.cn").read())
    IParser.getresult()
    IParser.close()
