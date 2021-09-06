import grequests

urls = [
    'http://localhost:8088/test/sendMessage?lockName=test&clear=false',
]


def method3():
    tasks = [grequests.get(u) for u in urls]
    res = grequests.map(tasks, size=6)
    print(res[0].text)


if __name__ == '__main__':
    for i in range(0, 10000):
        method3()
