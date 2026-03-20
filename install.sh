#!/bin/bash
sudo apt install build-essential patchelf 
python3 -m venv venv

source venv/bin/activate
sudo python3 install.py "$@"
deactivate
