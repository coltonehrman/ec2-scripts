#!/usr/bin/bash

mv /tmp/$1 /root/app
( cd /root/app && npm i --omit=dev )