#!/bin/sh

rm -f swcdocs/*.md 
rm -rf swcdocs/conflict swcdocs/lc

version=$(cat docs/index.md|grep '^This documentation was generated'|cut -f9 -d' ')
date=$(cat docs/index.md|grep '^This documentation was generated'|cut -f11 -d' ')
month=$(echo "$date"|cut -f1 -d/)
year=$(echo "$date"|cut -f3 -d/)
day=$(echo "$date"|cut -f2 -d/)
fulldate="20$year-$month-$day"
echo $fulldate
cp docs/*.md swcdocs/
cd swcdocs
mkdir -p conflict lc
for i in conflict_* ; do 
	j=${i##conflict_}
	mv $i conflict/$j
done
for i in lc_* ; do 
	j=${i##lc_}
	mv $i lc/$j
done
git add *
git commit -m "New docs version $version date $fulldate"
git push origin
