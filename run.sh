#!/bin/bash

git pull
venv/bin/python -m flask run --host=0.0.0.0 --port=80
