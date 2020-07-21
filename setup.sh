#!/bin/bash

git pull
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

echo "Update the service file, copy it to /etc/systemd/system, and enable it"
