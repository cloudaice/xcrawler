#-*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import redis
import cPickle as pickle
from tool import *

"""
使用cPickle模块速度会更加快
"""

class produce_req:
    def __init__(self,url,data={},headers={}):
        self.url = url
        self.data = data
        self.headers = headers

    def return_req(self,method):
        """produce req"""
        if not self.url:
            raise  "no url"
        if method=="GET":
            return urllib2.Request(url+"?")
        else:
            return urllib2.Request(url,urllib.urlencode(self.data),self.headers)

    def install_cookie(self):
        cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(opener)

    def install_proxy(self,proxyaddr):
        proxy_support = urllib2.ProxyHandler({"http":proxyaddr})
        opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
        urllib2.install_opener(opener)

    def install_cookies_proxy(self,proxyaddr):
        proxy_support = urllib2.ProxyHandler({"http":proxyaddr})
        cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        opener = urllib2.build_opener(proxy_support,cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(opener)


"""request_data is a dict and have these keys"""

"""
"id":
"url":
"method":
"req_data":
"headers":
"""


if __name__=="__main__":
    r = redis.Redis()
    url = "http://www.sina.com.cn"
    request_data = {"id":"001","url":url,"method":"GET"}
    for i in range(1000):
        into_redis(r,request_data,"linkbase")
        ids,url,method = out_redis(r,"linkbase")
        print ids,url,method
        req = produce_req(url)
        req = req.return_req(method)
        result = urllib2.urlopen(req)
        result=result.read().decode("gb2312","ignore").encode("utf-8")
        into_result_queue(r,"result_data",ids,result)
        print get_result_from_queue(r,"result_data",ids)
        #print result.info()

"""
定义url
"""
"""
url = "http://s.cloudaice.com"
"""
"""
产生getdata
具体要根据要抓取的信息来决定，
"""
"""
getdata = urllib.urlencode(
        {
            "key":"value",
            ......
            }
        )
"""

"""
产生postdata
具体内容也是根据要抓取的网页决定
"""
"""
postdata = urllib.urlencode (
        {
            "username":"",
            "password":"",
            "continueURL":"",
            "login_submit":""
            }
        )
"""

"""
设置header的信息
有些时候模仿浏览器来抓取网页
对付反盗链,有些网站会检查referer站点是不是他自己
header 就是一个dict，如果实在不行，使用httpfox抓取header之后全部填进去
"""
"""
headers= {"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5"
          "Referer":"http://s.cloudaice.com"
           .......
        }
"""

"""
cookie处理
使用代理抓取
"""
"""
cookie_support = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
proxy_support = urllib2.ProxyHandler({"http":"http://127.0.0.1:8087"})
opener = urllib2.build_opener(proxy_support,cookie_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)
"""

""" 生成http请求 """
"""get请求"""
"""
req =  urllib2.Request(url+"?"+getdata)
"""

"""post请求"""
"""
req = urllib2.Request(url,postdata,headers)
"""

"""返回抓取的句柄"""
"""
result = urllib2.urlopen(req)
result.getcode()
result.info()
result.geturl()
result.read()
"""

