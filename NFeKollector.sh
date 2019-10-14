#!/bin/sh

source venv/bin/activate
python NFeImport.py xml/ >> nfe.log
deactivate
