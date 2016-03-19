#! /usr/bin/env sh

DBNAME=$1
MAC=$2
shift;
shift;

SELECT=`cat $DBPATH"/"$DBNAME".db" | grep $MAC`
UPDATE=`echo $@ | sed "s/[ ]/\$/g"`


TMP_FILE=`mktemp /tmp/config.XXXXXXXXXX`
sed -e "s/$SELECT/$UPDATE/" $DBPATH"/"$DBNAME".db" > $TMP_FILE
mv $TMP_FILE $DBPATH"/"$DBNAME".db"
# sed -i "s/$SELECT/$UPDATE/g" $DBPATH"/"$DBNAME".db"


