#!/usr/bin/bash

mv /tmp/$1.zip /root/$1.zip
unzip /root/$1.zip -d /root/$1
( cd /root/$1 && npm i vite )