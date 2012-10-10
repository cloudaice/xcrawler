#-*- conding: utf-8 -*-
import redis
import sys
sys.path.append(sys.path[0]+'/../')
from xcrawler import *

r = redis.Redis()

produce_url(r)
