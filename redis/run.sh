redis-cli flushall
python inserting_redis.py
cat data.txt| redis-cli > out.txt
python calculating_redis_time.py
cat query.txt | redis-cli > qout.txt
