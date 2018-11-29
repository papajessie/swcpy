#!/bin/sh

START=${1:-1000}

if [ "$START" -lt 1190 ]; then
	SEQ="$(seq $START 1189) $(seq 2001 $(cat lastversion.txt))"
else
	SEQ="$(seq 2001 $(cat lastversion.txt))"
fi

echo $SEQ
exit

cd swcdocs/
if [ "$START" -le 1000 ]; then
    INDEX=5217d1edb2803d255c2856524bdda3472d754bf8
else
    INDEX=$(git log index.md|grep -B 4 "version $((START-1))"|grep ^commit | cut -c 8-)
    if [ -z "$INDEX" ]; then
        echo "Version $((START-1)) not found !"
        exit 1
    fi
fi
git reset --hard "$INDEX"
git push --force origin
cd ..

for i in $SEQ; do
    rm docs/*
    ./swc.py mode=docs version=$i
    rm -f swcdocs/*.md 
    rm -rf swcdocs/conflict swcdocs/lc swcdocs/ep

    version=$(cat docs/index.md|grep '^This documentation was generated'|cut -f9 -d' ')
    date=$(cat docs/index.md|grep '^This documentation was generated'|cut -f11 -d' ')
    month=$(echo "$date"|cut -f1 -d/)
    year=$(echo "$date"|cut -f3 -d/)
    day=$(echo "$date"|cut -f2 -d/)
    fulldate="20$year-$month-$day"
    echo $fulldate
    cp docs/*.md swcdocs/
    cd swcdocs
    mkdir -p conflict lc ep
    for i in conflict_* ; do 
	j=${i##conflict_}
	mv $i conflict/$j
    done
    for i in lc_* ; do 
	j=${i##lc_}
	mv $i lc/$j
    done
    for i in ep_* ; do 
	j=${i##ep_}
	mv $i ep/$j
    done

    BIG=$(git diff |wc -l)
    git add *
    git commit -m "New docs version $version date $fulldate ~$BIG"
    git push origin
    cd ../
done
