from flask import Flask
import os
dirname= os.getcwd()

app = Flask(__name__, static_folder=dirname)
@app.route("/")
def index():
    return "тут буде мій блог"
    app.run()