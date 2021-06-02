import redis

r = redis.StrictRedis(host='172.16.4.82', port=6379, db=0, password='smcaiot_redis_pass')
r.set('foo', 'bar')
print(r.get('foo'))
