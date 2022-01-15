# Simple Python-Flask REST API demo for use on CSC Rahti

## 1. On rahti.csc.fi Openshift Web Console:
- Create python-project on CSC Rahti (use github repo)
- Create the following environment variables (Builds/[your app]/Environment):
```
    MAIL_SMTP="smtp.pouta.csc.fi:25"
    MAIL_FROM="from addd" # Must be valid-ish!
    ALLOWED_MAILDOMAIN="@somedomain.com" # If you want to restrict which domains it can send to
```
- When the first build is complete, find the Webhook url (Builds/[your app]/Configuration)

## 2. On Github (setup push-to-deploy)
- Copy-paste the GitHub Webhook URL from Rahti to GitHub/Settings/Webhooks/New Webhook. 
- Set Webhook Content type to application/json

### Note
- Make sure your default branch is named `master` not `main`.
- Rahti wants your app to listen on port 8080

## POST /sendmail
```
{ 
    "to": "user@server.domain", 
    "subject": "Subject", 
    "body": "Body" 
}

