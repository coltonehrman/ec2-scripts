#!/usr/bin/bash

rm -rf /root/app
cp -r /tmp/$1 /root/app
( cd /root/app && npm i --omit=dev )