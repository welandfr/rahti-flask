# rahti-flask

## On rahti.csc.fi Openshift Web Console:
- Create python-project on CSC Rahti (use github repo)
- Create the following environment variables:
```
    MAIL_SMTP="smtp.pouta.csc.fi:25"
    MAIL_FROM="from addd" # Must be valid-ish!
    ALLOWED_MAILDOMAIN="@somedomain.com" # If you want to restrict which domains it can send to
```

## On Github
- Copy-paste the GitHub Webhook URL to GitHub/Settings/Webhooks/New Webhook. 
- Set Webhook Content type to application/json

## POST /sendmail
```
{ 
    "to": "user@server.domain", 
    "subject": "Subject", 
    "body": "Body" 
}