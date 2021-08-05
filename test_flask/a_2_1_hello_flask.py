from flask import Flask, jsonify
from test_mysql.my_pymysql import UsingMysql

app = Flask(__name__, instance_path='D:\workspace\myfile\repository\learnpy\testpy\test_flask\a_2_1_hello_flask.py')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/error')
def error_hello():
    x = 10
    y = 0
    res = x / y
    print(res)
    return 'Hello World!'


@app.route("/findAllStock", methods=['POST'])
def findAllStock():
    with UsingMysql() as um:
        sql = 'select * from test_stock_2021_07_31'
        ls = um.fetch_all(sql)
    return jsonify(ls)


def runapp():
    """
        如果没有 app.run() 方法，则需要执行下面指令启动
        shell:
            export FLASK_APP=test_flask.a_2_1_hello_flask.py
            flask run
        cmd:
            set FLASK_APP=test_flask.a_2_1_hello_flask.py
            flask run
        powershell:
            $env:FLASK_APP = "test_flask.a_2_1_hello_flask.py"
            flask run
        """
    app.run(debug=True)


if __name__ == '__main__':
    runapp()
