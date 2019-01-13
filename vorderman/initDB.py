import redis
import json

PORT=6379
PASSWORD = None

with open('conf/password') as f:
    PASSWORD = f.read().strip()

r = redis.Redis(host='redis', port=PORT, password=PASSWORD)
print ("Connected to db")

# Check if we need to populate the db
if r.exists('abd'):
    print ("Keys already exist, skipping db init")
    exit(0)

with open('data/words_dictionary.json') as f:
    raw = json.load(f)

print ("Populating db")
for word in raw.keys():
    if len(word) > 9:
        continue

    sortedWord = ''.join(sorted(word))
    if r.exists(sortedWord):
        r.append(sortedWord, ' '+word)
    else:
        r.set(sortedWord, word)
