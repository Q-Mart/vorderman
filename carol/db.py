import redis

class dataBase:
    def __init__(self):
        with open('conf/password') as f:
            PASSWORD = f.read().strip()
        self._r = redis.Redis(host='redis', password=PASSWORD)

    def __getitem__(self, key):
        return self._r.get(key).split()

    def __contains__(self, key):
        return bool(self._r.exists(key))
