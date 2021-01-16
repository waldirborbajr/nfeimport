#!/bin/bash

# while :; do python /nfeimport/NFeDownloadXML.py; sleep 60; done &
# while :; do python /nfeimport/NFeImport.py xml/; sleep 145; done &

cd /nfeimport/

# Download dos XMLs do email
echo "Download starting..."
/opt/venv/bin/python /nfeimport/NFeDownloadXML.py
echo "Download finished."

# Carga dos XMLs
echo "Import starting..."
/opt/venv/bin/python /nfeimport/NFeImport.py xml/
echo "Import finished."
