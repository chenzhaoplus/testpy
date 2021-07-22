import redis


def test_set():
    """
    key
    """
    r.set('foo', 'bar')
    print(r.get('foo'))


def test_sadd():
    """
    set
    """
    r.sadd("fdfs1:file1", "222")
    x = r.smembers("fdfs1:file1")
    print(x)


def test_delete():
    """
    delete
    """
    r.delete("fdfs1:file1")


def test_zadd():
    """
    zset
    """
    data_dict = {
        1: "111",
        2: "222",
    }
    for k, v in data_dict.items():
        member = v
        score = k
        mapping = {
            member: score,
        }
        r.zadd("fdfs:file", mapping)


def main():
    # test_set()
    # test_delete()
    # test_sadd()
    test_zadd()


if __name__ == '__main__':
    r = redis.StrictRedis(host='172.16.4.82', port=6379, db=0, password='smcaiot_redis_pass')
    main()
