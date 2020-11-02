#!/bin/sh

# while :; do python /nfeimport/NFeDownloadXML.py; sleep 60; done &
# while :; do python /nfeimport/NFeImport.py xml/; sleep 120; done &

# Download dos XMLs do email
watch -n 60 python /nfeimport/NFeDownloadXML.py

# Carga dos XMLs
watch -n 120 python /nfeimport/NFeImport.py xml/