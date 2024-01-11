#!/usr/bin/bash

rm -rf /root/$1
cp -r /tmp/$1-$2 /root/$1
( cd /root/$1 && npm i --omit=dev )