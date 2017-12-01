from flask import Flask
import json



app = Flask(__name__)


@app.route("/",methods=['GET'])
def hello_world():
    return "Hello World!"

@app.route("/<string:name>")
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
        app.run(host='0.0.0.0',port=8081, debug=False)
        

