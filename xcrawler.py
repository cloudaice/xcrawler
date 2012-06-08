#-*- coding:utf-8 -*-
from gevent import monkey
monkey.patch_all()

import urllib2
import urllib
import cookielib
import gevent
from gevent.queue import Queue,Empty


url=["http://www.baidu.com","http://s.cloudaice.com","http://www.sina.com.cn","http://www.163.com"]
req_queue=Queue(maxsize = 3)
def deal_req(workername):
    try:
        while True:
            req = req_queue.get(timeout=1)
            response = urllib2.urlopen(req)
            print response.getcode()
            req.close()
    except Empty:
        print "req_queue is empty",workername

def produce_req():
    for i in range(4):
        req_queue.put(url[i])
    print "all right"

gevent.joinall([
    gevent.spawn(produce_req),
    gevent.spawn(deal_req,"thread1"),
    gevent.spawn(deal_req,"thread2"),
    gevent.spawn(deal_req,"thread3"),
            ])


