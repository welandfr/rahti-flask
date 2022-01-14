import os
from flask import Flask, jsonify

# Create Flask instance
app = Flask(__name__)

@app.route("/")
def index():
    ret = {'messgage': 'Hello'}

    return jsonify(ret)

if __name__ == "__main__":
    app.run(debug=True,
            port=8080,
            host='0.0.0.0')
