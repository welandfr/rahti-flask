# rahti-flask

- Create python-project on CSC Rahti
- Copy-paste the GitHub Webhook URL to GitHub/Settings/Webhooks/New Webhook. 
- Set Webhook Content type to application/json


## POST /sendmail
```
{ 
    "to": "user@server.domain", 
    "subject": "Subject", 
    "body": "Body" 
}