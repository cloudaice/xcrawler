#-*- coding: utf-8 -*-
import redis
import sys
sys.path.append(sys.path[0]+'/../')
from xcrawler import *
r = redis.Redis()
do_main(r,100)


