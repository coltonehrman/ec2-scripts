#!/usr/bin/bash

mv /tmp/$1 /root/$1
( cd /root/$1 && npm i --omit=dev )