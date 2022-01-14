import os
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    ret = {'messgage': 'Hello', 'smtp': os.environ.get('MAIL_SMTP')}

    return jsonify(ret)

if __name__ == "__main__":
    app.run(debug=True,
            port=8080,
            host='0.0.0.0')
