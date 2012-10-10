#-*- coding:utf-8 -*-
import cPickle as pickle
from time import *
import gevent.pool
from geventhttpclient import HTTPClient,URL
from geturl import *
from testcode import *
import redis


def run(client,url):
    print "do req"
    try:
        response = client.get(url.request_uri)
        result=response.read()
        emcode = test_website(url.request_uei)
        result = result.decode(encode,'ignore').encode("utf-8")
        p = pickle.dumps(result)
        r.lpush("htmlbase",p)
        print "push done"
        #print response.status_code
        assert response.status_code == 200
        print response.status_code
        client.close()
    except :
        print "time out"
        

def produce_url(r):
    while True:
        t = r.rpop('htmlbase')
        while not t:
            print "empty"
            sleep(1)
            t = r.rpop('htmlbase')
        data = pickle.loads(t)
        IParser = parselinks()
        IParser.feed(data)
        IParser.saveurl(r)
        IParser.close()
        print 'done'


def gethtml(r):
    while True:
        t = r.rpop('htmlbase')
        while not t:
            sleep(0.1)
            t = r.rpop('htmlbase')
        data = pickle.loads(t)
        print data[0:10]

def do_main(r,C):
    group = gevent.pool.Pool(size = C)
    while True:
        t = r.rpop('urllist')
        while not t:
            print "empty"
            sleep(0.1)
            t = r.rpop('urllist')
        #url = pickle.loads(t)
        url = t
        url = URL(url)
        print url.request_uri
        client = HTTPClient.from_url(url,concurrency = C,connection_timeout=100,network_timeout=10)
        group.spawn(run,client,url)
        print "spawn"

    group.join()

if __name__ == "__main__":
    r = redis.Redis()
    #produce_url(r)
    do_main(r,100)

    
