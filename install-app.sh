#!/usr/bin/bash

rm -rf /root/$1
cp -r /tmp/$1-$2 /root/$1

if [ "$3" = "true" ]; then
    echo "is true" 
    ( cd /root/$1 && npm i --omit=dev )
fi