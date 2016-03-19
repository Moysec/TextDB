#! /usr/bin/env sh

DBNAME=$1
shift;
SELECT=`echo $@ | sed "s/[ ]/\$/g"`
echo `cat $DBPATH/$DBNAME".db" | grep  "$SELECT"`
