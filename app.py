import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return os.environ.get("MESSAGE", "Hello IBM conference!")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
