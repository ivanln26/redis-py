import redis
import time

r = redis.Redis(host='redis', port='6379', db=0)

i = 0

while True:
    r.publish('canal', f'mensaje {i}')
    print(f'Mensaje: {i}')
    i += 1
    time.sleep(5)
