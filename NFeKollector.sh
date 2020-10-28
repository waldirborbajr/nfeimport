#!/bin/sh

# source venv/bin/activate
python NFeImport.py xml/ >> nfe.log
# deactivate


# while python NFeImport.py xml/ >> nfe.log; do sleep 300; done

# while :; do python NFeImport.py xml/ >> nfe.log; sleep 300; done