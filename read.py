import redis
import time

r = redis.Redis(host='redis', port='6379', db=0)
p = r.pubsub()
p.subscribe('canal')

while True:
    message = p.get_message()
    print(message)
    time.sleep(10)
