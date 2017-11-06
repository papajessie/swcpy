#!/bin/sh
git pull origin
./swc.py mode=docs

if [ -n "$1" ]; then
    git add docs
    git commit -m 'Update docs'
    git push origin
fi
