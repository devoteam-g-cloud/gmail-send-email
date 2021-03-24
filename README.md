## Gmail API

This project's aim is to have a minimal template to send an email using the Gmail API.

## Requirements
- Have a service account key (name it `service-account.json` and add it to the project root)

- Have the Gmail API activated on the GCP project

- Authorize the needed scope on your Workspace platform: `https://www.googleapis.com/auth/gmail.send`

- Have Python3, Python virtualenv and pip installed

## Setup
- create a virtualenv : `python3 -m venv venv`

- activate venv : `source venv/bin/activate`

- install requirements: `pip install -r requirements.txt`
