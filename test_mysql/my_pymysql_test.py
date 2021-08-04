from my_pymysql import UsingMysql


def select_one(cursor):
    cursor.execute("select * from Product")
    data = cursor.fetchone()
    print("-- 单条记录: {0} ".format(data))


# 新增单条记录
def create_one():
    with UsingMysql(log_time=True) as um:
        sql = "insert into Product(name, remark) values(%s, %s)"
        params = ('男士双肩背包1', '这个是非常好的背包')
        um.cursor.execute(sql, params)

        # 查看结果
        select_one(um.cursor)


def check_it():
    with UsingMysql(log_time=True) as um:
        sql = "select count(id) as total from Product"
        print("-- 当前数量: %d " % um.get_count(sql, None, 'total'))


def get_count(cursor):
    cursor.execute("select count(id) as total from Product")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()

    print("-- 当前数量: %d " % data['total'])


def delete_all(cursor):
    cursor.execute("delete from Product")


def create_many():
    with UsingMysql(log_time=True) as um:
        # 清空之前的测试记录
        delete_all(um.cursor)

        for i in range(0, 1000):
            sql = "insert into Product(name, remark) values(%s, %s)"
            params = (f'男士双肩背包{i}', f'这个是非常好的背包{i}')
            um.cursor.execute(sql, params)

        # 查看结果
        get_count(um.cursor)


def delete_one(cursor, name):
    sql = 'delete from Product where name = %s'
    params = name
    cursor.execute(sql, params)
    print('--- 已删除名字为%s的商品. ' % name)


def select_one(cursor):
    sql = 'select * from Product'
    cursor.execute(sql)
    data = cursor.fetchone()
    print('--- 已找到名字为%s的商品. ' % data['name'])
    return data['name']


def select_one_by_name(cursor, name):
    sql = 'select * from Product where name = %s'
    params = name
    cursor.execute(sql, params)
    data = cursor.fetchone()
    if data:
        print('--- 已找到名字为%s的商品. ' % data['name'])
    else:
        print('--- 名字为%s的商品已经没有了' % name)


# 删除单条记录
def check_delete_one():
    with UsingMysql(log_time=True) as um:
        # 查找一条记录
        name = select_one(um.cursor)

        # 删除之
        delete_one(um.cursor, name)

        # 查看还在不在?
        select_one_by_name(um.cursor, name)


def update_by_pk(cursor, name, pk):
    sql = "update Product set name = '%s' where id = %d" % (name, pk)

    cursor.execute(sql)


def select_one(cursor):
    sql = 'select * from Product'
    cursor.execute(sql)
    return cursor.fetchone()


def select_one_by_name(cursor, name):
    sql = 'select * from Product where name = %s'
    params = name
    cursor.execute(sql, params)
    data = cursor.fetchone()
    if data:
        print('--- 已找到名字为%s的商品. ' % data['name'])
    else:
        print('--- 名字为%s的商品已经没有了' % name)


# 修改记录
def check_update():
    with UsingMysql(log_time=True) as um:
        # 查找一条记录
        data = select_one(um.cursor)
        pk = data['id']
        print('--- 商品{0}: '.format(data))

        # 修改名字
        new_name = '单肩包'
        update_by_pk(um.cursor, new_name, pk)

        # 查看
        select_one_by_name(um.cursor, new_name)


def fetch_list_by_filter(cursor, pk):
    sql = 'select * from Product where id > %d' % pk
    cursor.execute(sql)
    data_list = cursor.fetchall()
    print('-- 总数: %d' % len(data_list))
    return data_list


# 查找
def fetch_list():
    with UsingMysql(log_time=True) as um:
        # 查找id 大于800的记录
        data_list = fetch_list_by_filter(um.cursor, 800)

        # 查找id 大于 10000 的记录
        data_list = fetch_list_by_filter(um.cursor, 10000)


def fetch_page_data(cursor, pk, page_size, skip):
    sql = 'select * from Product where id > %d limit %d,%d' % (pk, skip, page_size)
    cursor.execute(sql)
    data_list = cursor.fetchall()
    print('-- 总数: %d' % len(data_list))
    print('-- 数据: {0}'.format(data_list))
    return data_list


# 查找
def check_page():
    with UsingMysql(log_time=True) as um:
        page_size = 10
        pk = 500

        for page_no in range(1, 6):
            print('====== 第%d页数据' % page_no)
            skip = (page_no - 1) * page_size

            fetch_page_data(um.cursor, pk, page_size, skip)


if __name__ == '__main__':
    # create_one()
    # create_many()
    # check_delete_one()
    # check_update()
    # fetch_list()
    check_page()
    # check_it()
