import redis
import time

r = redis.Redis(host='localhost', port='6379', db=0)
p = r.pubsub()
p.subscribe('canal')

while True:
    message = p.get_message()
    if message:
        print(message['data'])
    time.sleep(1)
