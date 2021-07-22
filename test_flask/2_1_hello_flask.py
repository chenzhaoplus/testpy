from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    """
    如果没有 app.run() 方法，则需要执行下面指令启动
    shell:
        export FLASK_APP=test_flask
        flask run
    cmd:
        set FLASK_APP=test_flask
        flask run
    powershell:
        $env:FLASK_APP = "test_flask"
        flask run
    """
    app.run()
