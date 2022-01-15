# Simple Python-Flask REST API demo for use on CSC Rahti

## 1. On rahti.csc.fi Openshift Web Console:
- Create python-project on CSC Rahti (use github repo)
- Set any environment variables you need, Builds/[your app]/Environment
- When the first build is complete, find the Webhook url (Builds/[your app]/Configuration)

## 2. On Github (setup push-to-deploy)
- Copy-paste the GitHub Webhook URL from Rahti to GitHub/Settings/Webhooks/New Webhook. 
- Set Webhook Content type to application/json

### Note
- Make sure your default branch is named `master` not `main`.
- Rahti wants your app to listen on port 8080
- To run you app over SLL (https) just enable it in you Route (Applications/Routes) by enabling "Secure Route".
- The `.devcontainer` folder is a VSCode thing, not needed for Rahti. 


