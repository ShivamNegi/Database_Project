import redis
import time
from random import randrange as rr

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

total_time = 0
for i in range(10**4):
    key = "channel" + `rr(1, 10**4)`
    start = time.time()
    r.lrange(key, 0, -1)
    end = time.time()
    total_time += end - start
            
print "Query execution time in seconds:", total_time
