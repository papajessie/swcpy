#!/bin/sh

if [ "$SILENT" != "1" ]; then
    SILENT=0
fi

if [ -n "$2" ]; then
    PREFIX="$2"
else
    PREFIX="."
fi

if [ -n "$2" ]; then
    SUFFIX="$3"
else
    SUFFIX="."
fi

if [ -n "$1" ]; then
    VERSION=$1
    echo "Downloading version $VERSION"
else
    echo "Let us look for the last version..."
    VERSION=1012
    if [ -f lastversion.txt ]; then
        VERSION=$(cat lastversion.txt)
    fi
    FOUND=0
    LASTDEST="/tmp/nonexistent"
    while [ "$FOUND" = 0 ]; do
        LASTVERSION=$VERSION
        VERSION=$((VERSION+1))
        # MANIFEST="https://starts0.content.disney.io/cloud-cms/manifest/starts/prod/${VERSION}.json" # oldstyle
        MANIFEST="https://d50ea5a0.content.disney.io/manifests/__manifest_starts_prod.0${VERSION}.json"
        DEST=manifest${VERSION}.json
        curl -s -o "$DEST" "$MANIFEST"
        if  [ "$(stat -c %s $DEST)" -lt 20000 ]; then
            FOUND=1
            echo "Version $VERSION is not available. Going back to $LASTVERSION."
            VERSION="$LASTVERSION"
        else
            rm -f $LASTDEST
            LASTDEST=$DEST
            echo "$VERSION found"
            echo "$VERSION" > lastversion.txt
        fi
    done
fi

if [ -n "$VCHECK" ]; then
    exit 0
fi

MANIFEST="https://d50ea5a0.content.disney.io/manifests/__manifest_starts_prod.0${VERSION}.json"
DEST=manifest${VERSION}.json
if [ '!' -f "$DEST" ]; then
    curl -o "$DEST" "$MANIFEST"
fi

if  [ "$(stat -c %s $DEST)" -lt 20000 ]; then
    echo "Version $VERSION is not available."
    rm -f $DEST
    exit 0
fi


mkdir -p content/$VERSION
MANIFESTJSON=content/$VERSION/MANIFEST.json
json_pp < $DEST > $MANIFESTJSON
PRODID=$(grep productId $MANIFESTJSON|cut -f4 -d\")
ENVIRONMENT=$(grep '"environment"' $MANIFESTJSON|head -n 1|cut -f4 -d\")
CDNROOT=$(grep cdnRoot $MANIFESTJSON|grep https|cut -f4 -d\")

ROOTURL="$CDNROOT"
echo "$ROOTURL"
N=0

cat $MANIFESTJSON |sed -ne '/^   "paths"/,/^   },/ p'|grep '^      "'|cut -f2 -d'"' > $MANIFESTJSON.ids
cat $MANIFESTJSON |sed -ne '/^   "paths"/,/^   },/ p'|grep '^         "v"'|cut -f12 -d' '|sed -e 's/,$//g' > $MANIFESTJSON.versions
paste -d: $MANIFESTJSON.ids $MANIFESTJSON.versions > $MANIFESTJSON.lines
M=$(wc -l < $MANIFESTJSON.lines)

cat $MANIFESTJSON.lines|sort -r|while read line; do
    N=$((N+1))
    XPATH=$(echo "$line"|cut -f1 -d:)
    if [ $(echo "$XPATH"| grep "^${PREFIX}.*${SUFFIX}$"|wc -l) -gt 0 ]; then
        if [ -n "$UNSAFE" ]||[ "${XPATH%.assetbundle}${XPATH%.joe}" = "${XPATH}${XPATH}" ]; then
            FILENAME=$(basename $XPATH)
            HASH=$(echo "$line"|cut -f2 -d:)
            URL="$ROOTURL/$HASH/$XPATH"
            mkdir -p content/$VERSION/$(dirname $XPATH)
            if [ "$SILENT" = 0 ]; then
		echo -n "$N/$M: $XPATH"
	    fi
            if [ ! -f content/${VERSION}/${XPATH} ]; then
                if [ "$SILENT" = 0 ]; then
                    echo " X"
	        fi
                curl -s -o content/${VERSION}/${XPATH} "$URL" > /dev/null
            else
                if [ "$SILENT" = 0 ]; then
                    echo " OK"
	        fi
            fi
        fi
    fi
done

