import redis
import time
from random import randrange as rr

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

for k in range(4):
    total_time = 0
    x, y = map(int, raw_input().strip().split())
    print "Running for", x, y

    r.flushall()
    for i in range(10**x):
        key = "channel" + `i`
        for j in range(10**y):
            value = "user" + `j`
            start = time.time()
            r.lpush(key, value)
            end = time.time()
            total_time += end - start
                
    print "Inserting Module timing:", total_time
    print

    total_time = 0
    for i in range(10**4):
        key = "channel" + `rr(10**x)`
        start = time.time()
        r.lrange(key, 0, -1)
        end = time.time()
        total_time += end - start
                
    print "Query execution time in seconds:", total_time
    print
