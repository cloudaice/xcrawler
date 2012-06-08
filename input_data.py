#-*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib

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
            return urllib2.Request(url+"?"+urllib.urlencode(self.data),headers)
        else:
            return urllib2.Request(url,urllib.urlencode(self.data),headers)

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

if __name__=="__main__":
    data= {
            'BH': "0903101",
            'submit': '查询课表'.decode('utf-8').encode('gb2312'),
          }
    url = "http://xscj.hit.edu.cn/HitJwgl/XS/kfxqkb.asp"
    headers= {
           "User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        }
    req = produce_req(url,data,headers)
    req = req.return_req("POST")
    result = urllib2.urlopen(req)
    print result.read().decode("gb2312","ignore").encode("utf-8")

































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

"""
生成http请求
"""
"""get请求"""
req =  urllib2.Request(url+"?"+getdata)

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

