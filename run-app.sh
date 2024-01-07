#!/usr/bin/bash

cd /root/app
nohup npm run start > /var/log/app/out.log 2> /var/log/app/err.log &