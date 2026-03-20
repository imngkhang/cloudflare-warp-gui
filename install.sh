#!/bin/bash

python3 -m venv venv

source venv/bin/activate
sudo python3 install.py "$@"
deactivate
