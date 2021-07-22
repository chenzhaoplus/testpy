import redis

r = redis.StrictRedis(host='172.16.4.82', port=6379, db=0, password='smcaiot_redis_pass')

"""
key
"""
# r.set('foo', 'bar')
# print(r.get('foo'))

"""
set
"""
# r.sadd("fdfs1:file1", "222")
# x = r.smembers("fdfs1:file1")
# print(x)

"""
delete
"""
r.delete("fdfs:file")

"""
zset
"""
# data_dict = {
#     "111": 1,
#     "222": 2,
# }
# for d, x in data_dict.items():
#     score = d
#     member = str(x)
#     mapping = {
#         member: score,
#     }
#     r.zadd("fdfs1:file1", mapping)  # 正确
