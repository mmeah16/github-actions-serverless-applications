import json
from flask import Flask 
from mangum import Mangum
# import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "message": "hello world",
    }), 200

handler = Mangum(app)

if __name__ == "__main__":
    app.run()
