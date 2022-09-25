#!/bin/bash
python3 main.py

if [[-x '$(command -v python3)']]
then
    
else
  echo 'Error: 
    This program runs on Python 3, it appears Python 3 is not installed.
    To install Python 3, check out https://www.python.org/downloads/ 
    and run this script again' >&2
  exit 1
fi