#!/usr/bin/bash

cp -r /tmp/$1 /root/app
( cd /root/app && npm i --omit=dev )