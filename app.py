import os, smtplib
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    ret = {'message': 'This is the email service.' }

    return ret


@app.route("/sendmail", methods = [ 'POST' ])
def send():
    ret = { 'smtp': os.environ.get('MAIL_SMTP')}

    req = request.get_json()

    msg = f"""From: {os.environ.get('MAIL_FROM')}
        To: {req['to']}
        Subject: {req['subject']}

        {req['body']}"""

    try:
        smtp_obj = smtplib.SMTP(os.environ.get('MAIL_SMTP'))
        smtp_obj.sendmail(req['from'], [req['to']], msg)

        ret = { 'message': 'Mail sent' }

    except Exception as e:
        ret =  { 'error': 'Mail fail.' }
        print(e)
    
    return ret

if __name__ == "__main__":
    app.run(debug=True,
            port=8080,
            host='0.0.0.0')
