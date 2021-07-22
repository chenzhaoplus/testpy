import os
import datetime
import re
import redis

# fdfs_path = 'group1/M00'
fdfs_path = 'M00'


def get_fdfs_file(base_path='/var/lib/fast-dfs/storage/path0/data'):
    with open('/ops/app/fdfs_url.txt', 'w') as f:
        cnt = 1
        for dir_path, dir_names, file_names in os.walk(base_path):
            """
            dir_path = /var/lib/fast-dfs/storage/path0/data
            dir_path = /var/lib/fast-dfs/storage/path0/data/00
            dir_path = /var/lib/fast-dfs/storage/path0/data/00/00
            
            dir_name = 00
            
            file_name = rBAEUl1s-HSAJNJ8AAAAAAAAAAA529.jpg
            """
            if cnt == 1:
                cnt += 1
                continue
            # print('dir_path = ' + dir_path)
            # for dir_name in dir_names:
            #     print('dir_name = ' + dir_name)
            # for file_name in file_names:
            #     print('file_name = ' + file_name)
            # print(f'file_names = {file_names}')
            # f.write('dir_path = ' + dir_path + '\n')
            # f.write('dir_names = ' + dir_name for dir_name in dir_names)
            # f.write('file_names = ' + file_name for file_name in file_names)

            for file in file_names:
                try:
                    paths = re.search(r'/var/lib/fast-dfs/storage/path0/data(.*)', dir_path).group(1)
                    # paths = /07/CA
                    # print("paths = " + paths)
                    # file = rBAEUl38lFSAEsQTAAJMnMh33HY041.png
                    # print("file = " + file)
                    full_path = os.path.join(fdfs_path + paths, file)
                    # print(full_path)
                    # f.write(full_path + '\n')
                    # r.sadd("fdfs:file", full_path)
                    mapping = {
                        full_path: int(cnt - 1),
                    }
                    r.zadd("fdfs:file", mapping)
                except:
                    pass

            cnt += 1


def start_tm():
    return datetime.datetime.now()


def end_tm(start_time=None):
    end_time = datetime.datetime.now()
    print("total time: " + str((end_time - start_time).microseconds / 1000) + "ms")


if __name__ == '__main__':
    start = start_tm()

    r = redis.StrictRedis(host='172.16.4.82', port=6379, db=0, password='smcaiot_redis_pass')
    get_fdfs_file()

    end_tm(start)
