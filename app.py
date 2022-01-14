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
    mail_from = os.environ.get('MAIL_FROM')
    mail_to = [req['to']]

    msg = f"""From: {mail_from}
        To: {mail_to[0]}
        Subject: {req['subject']}

        {req['body']}"""

    try:
        smtp_obj = smtplib.SMTP(os.environ.get('MAIL_SMTP'))
        smtp_obj.sendmail(mail_from, mail_to, msg)

        print(f"Mail sent to {mail_to[0]} using {os.environ.get('MAIL_SMTP')}")
        ret = { 'message': 'Mail sent' }

    except Exception as e:
        ret =  { 'error': 'Mail fail.' }, 500
        print(e)
    
    return ret

if __name__ == "__main__":
    app.run(debug=True,
            port=8080,
            host='0.0.0.0')
