import redis

PORT=6379

r = redis.Redis(host='redis', port=PORT)
