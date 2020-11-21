#!/bin/bash

# crond -b -l 8 -L /var/log/cron.log
crond -b -L /var/log/cron.log

crontab /nfeimport/cronfile