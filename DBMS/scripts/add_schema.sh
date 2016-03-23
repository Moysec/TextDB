#! /usr/bin/env sh
MODELNAME=$1
shift;
INSERT=`echo $@ | sed "s/[ ]/\$/g"`

echo $INSERT >> $MODELPATH"/"$MODELNAME".sch"
