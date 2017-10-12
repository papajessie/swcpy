#!/bin/sh


for i in "$@"; do ./swc.py version=${i} mode=translate|sort > /tmp/s${i};./swc.py version=${i} mode=tableitem|sort > /tmp/r${i};done 
