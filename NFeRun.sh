#!/bin/bash

# while :; do python /nfeimport/NFeDownloadXML.py; sleep 60; done &
# while :; do python /nfeimport/NFeImport.py xml/; sleep 145; done &

cd /nfeimport/

# Download dos XMLs do email
/opt/venv/bin/python /nfeimport/NFeDownloadXML.py

# Carga dos XMLs
/opt/venv/bin/python /nfeimport/NFeImport.py xml/