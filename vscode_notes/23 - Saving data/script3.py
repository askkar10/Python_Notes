# nosql databases
# key value store with redis
# redis is an in networked key-value store
# reis is commonly used for cachong, as an message broker, and for quick lookups of informations
# pip install redi
# trzeba sie zarejestrowac na stronie redisa i ogarnac database

"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='...',
    port=1..,
    decode_responses=True,
    username="...",
    password="...",
)

# print(r.keys())
# r.set('a_key','my value')
# print(r.keys())
# v = r.get('a_key')
# print(v)
# r.incr('counter')
# print(r.get('counter'))
# r.incr('counter')
# print(r.get('counter'))
# print(r.keys())

# example up -> how to set a key wit a value and how to set a key with a 'counter' variable and inrement int
# 'incr' method to add 1 to the urrent value of a key
# the following examples deal with  storing arrays or list
# r.rpush('words','one')
# r.rpush('words','two')
# print(r.lrange('words',0,-1))
# r.rpush('words','three')
# print(r.lrange('words',0,-1))
# print(r.llen('words'))
# r.lpush('words','zero')
# print(r.lrange('words',0,-1))
# print(r.lrange('words',3,3))
# print(r.lindex('words',1))
# print(r.lindex('words',2))

# rpush() -> pushing from the right
# lrange() -> giving the key, both a starting index and an ending index, with -1 idicatory the end of the list
# lpush() -> add to the beginning - left side
# lindex() -> retrieve single value
# llen() -> return length of list

# expiration of values:

# r.setex('timed',10,'10 seconds')
# print(r.pttl('timed'))
# print(r.pttl('timed'))
print(b'timed' in r.keys())
print(r.keys())

# setex() -> ustawia co do usuniecie i ile czasu w sekundach
# pttl() -> pokazuje w milisekundach ile czasu zostalo, -2 to znaczy ze juz zostalo usuniete