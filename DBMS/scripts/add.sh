#! /usr/bin/env sh
DBNAME=$1
shift;
INSERT=`echo $@ | sed "s/[ ]/\$/g"`

echo $INSERT >> $DBPATH"/$DBNAME.db"
