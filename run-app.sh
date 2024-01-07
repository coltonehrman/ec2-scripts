#!/usr/bin/bash

cd /root/app
fuser -k 80/tcp
nohup npm run start > /dev/null 2>&1 &