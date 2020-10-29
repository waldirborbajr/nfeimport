#!/bin/sh

# source venv/bin/activate
# python NFeImport.py xml/ >> nfe.log
# deactivate

# Executa de 30 em 30 minutos
while :; do python NFeImport.py xml/ >> log/nfe.log; sleep 1800; done