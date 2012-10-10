#-*- coding: utf-8 -*-

#这里可以把redis的连接符号当成参数传进去
import redis
import cPickle as pickle
def into_redis(r,request_data,listname):
    """使用序列化方法存储到redis的list中，并且将list作为一个queue"""
    #r = redis.Redis()
    p = pickle.dumps(request_data)
    r.lpush(listname,p)


def out_redis(r,listname):
    """从redis数据库中取出序列化的数据，并且进行解序列化"""
    #r = redis.Redis()
    t=r.rpop(listname)
    data = pickle.loads(t)
    return (data["id"],data["url"],data["method"])

def into_result_queue(r,hashname,ids,result_data):
    """将返回的网页结果存储到redis中去"""
    #r = redis.Redis()
    r.hset(hashname,ids,result_data)

def get_result_from_queue(r,hashname,ids):
    """docstring for get_result_from_queue"""
    #r = redis.Redis()
    return  r.hget(hashname,ids)
