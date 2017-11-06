import redis
import ast
import time

max = 4445
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

# code for deleting key
for i in range(1, max + 1):
    key = 'user' + `i`
    r.delete(key)

# inserting hash map into redis
counter = 1
time_elapsed = 0
with open('../mongodb_data.txt', 'r') as f1:
    for line in f1.readlines():
        key = 'user' + `counter`
        value = ast.literal_eval(line)
        start = time.time()
        r.hmset(key, value)
        end = time.time()
        time_elapsed = time_elapsed + end - start
        counter = counter + 1

print counter
print "Total Time Taken: " + `time_elapsed`
