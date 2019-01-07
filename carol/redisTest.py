import redis

PORT=6379
PASSWORD = None

with open('conf/password') as f:
    PASSWORD = f.read().strip()

r = redis.Redis(host='redis', port=PORT, password=PASSWORD)
print(r.get('foo'))
print (r.save())
