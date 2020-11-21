#!/bin/bash

while :; do python /nfeimport/NFeDownloadXML.py; sleep 60; done &
while :; do python /nfeimport/NFeImport.py xml/; sleep 145; done &

# Download dos XMLs do email
# /opt/venv/bin/python NFeDownloadXML.py

# Carga dos XMLs
# /opt/venv/bin/python NFeImport.py xml/