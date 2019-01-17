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

urlmanifest () {
    v="$1"
    if [ "$v" -ge 2000 ]; then
        url="http://zynga-swc-prod-1-seed.akamaized.net/manifests/__manifest_zyngaswc_prod.0${VERSION}.json"
        echo "$url"
    elif [ "$v" -ge 1000 ]; then
        url="https://d50ea5a0.content.disney.io/manifests/__manifest_starts_prod.0${VERSION}.json"
        echo "$url"
    else
        url="https://starts0.content.disney.io/cloud-cms/manifest/starts/prod/${VERSION}.json" # oldstyle
        echo "$url"
    fi
}

if [ -n "$1" ]; then
    VERSION=$1
    if [ "$SILENT" = 0 ]; then
        echo "Downloading version $VERSION"
    fi
else
    if [ "$SILENT" = 0 ]; then
        echo "Let us look for the last version..."
    fi
    VERSION=1012
    if [ -f lastversion.txt ]; then
        VERSION=$(cat lastversion.txt)
    fi
    FOUND=0
    LASTDEST="/tmp/nonexistent"
    while [ "$FOUND" = 0 ]; do
        LASTVERSION=$VERSION
        VERSION=$((VERSION+1))
        if [ "$VERSION" = 1190 ]; then
            VERSION=2001
        fi
        MANIFEST=$(urlmanifest "$VERSION")
        DEST=manifest${VERSION}.json
        curl -s -o "$DEST" "$MANIFEST"
        if  [ "$(stat -c %s $DEST)" -lt 20000 ]; then
            FOUND=1
            if [ "$SILENT" = 0 ]; then
                echo "Version $VERSION is not available. Going back to $LASTVERSION."
            fi
            VERSION="$LASTVERSION"
        else
            rm -f $LASTDEST
            LASTDEST=$DEST
            if [ "$SILENT" = 0 ]; then
                echo "$VERSION found"
            fi
            echo "$VERSION" > lastversion.txt
        fi
    done
fi

if [ -n "$VCHECK" ]; then
    exit 0
fi

MANIFEST=$(urlmanifest "$VERSION")
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

