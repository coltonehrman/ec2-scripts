#!/usr/bin/bash

cd /root/coltonehrman.com
nohup npm run start > /var/log/app/out.log 2> /var/log/app/err.log &