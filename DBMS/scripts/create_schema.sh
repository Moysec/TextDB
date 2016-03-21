#! /usr/bin/env sh
DBNAME=$1
SCHEMAPATH=$MODELPATH"/"$DBNAME".sch"
shift;
touch $SCHEMAPATH
INSERT=`echo $@ | sed "s/[ ]/\$/g"`

echo $INSERT >> $SCHEMAPATH 
