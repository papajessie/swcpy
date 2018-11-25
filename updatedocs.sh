#!/bin/sh
git pull origin
./swc.py mode=docs

a=$(cat lastversion.txt)

a=$(( a+1-1 ))
if [ -n "$1" ]; then
    git add docs
    git commit -m "Update docs ${a}"
    git push origin
fi
