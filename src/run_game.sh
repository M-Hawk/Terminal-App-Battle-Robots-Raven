#!/bin/bash

python3 -m pip install --user --upgrade pip # installs python package manager
python3 -m venv .venv # created a virtual environment
source .venv/bin/activate # activates a virtual environment
python3 -m pip install simple-term-menu # installs simple-term-menu module
python3 -m pip install art==5.7 # installs art module
python3 -m pip install colorama # installs colorama module
python3 main.py # runs game script
deactivate # deactivates virtual environment