import os

from flask import Flask

app = Flask(__name__, instance_path="D:\\workspace\\myfile\\repository\\learnpy\\testpy\\test_flask")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def runapp():
    print(f'instance_path = {app.instance_path}')
    filename = os.path.join(app.instance_path, 'templates\\404.html')
    with open(filename) as f:
        print(f.read())
    app.run(debug=True)


if __name__ == '__main__':
    runapp()
