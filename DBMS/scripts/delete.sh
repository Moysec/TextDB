#! /bin/bash

DBNAME=$1
shift;
DELETE=`echo $@ | sed "s,[ ],\$,g"`
sed  -i '/'$DELETE'/d' "$DBPATH/$DBNAME.db"
