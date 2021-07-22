from flask import Flask

app = Flask(__name__)

"""
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


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
