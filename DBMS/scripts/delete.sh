#! /bin/bash

#DBNAME=$1
#shift;
#DELETE=`echo $@ | sed "s,[ ],\$,g"`
#sed  -i '/'$DELETE'/d' "$DBPATH/$DBNAME.db"

DBNAME=$1
wantedfield=$2
data=$3
field=`awk -v wanted="$wantedfield" 'BEGIN{ FS="$"; } 
{ for(fn=1;fn<=NF;fn++) {if($fn == wanted) print fn;}; exit; }
         ' $MODELPATH/$DBNAME".sch"`
matched_lines=`awk -v field=$field 'BEGIN{FS="$";} {print $field;}' $DBPATH/$DBNAME".db" | sed -n "/$data/="`
#matched_lines=`echo $matched_lines | sed 's/[ ]/,/g'`
#del_line_num=${matched_lines[0]}
#del_line_num=`echo $matched_lines | awk '{print $1}'`
line_decr=0
for line_num in $matched_lines
do
    sed -i "$((line_num - line_decr))d" $DBPATH/$DBNAME".db"
    line_decr=$((++line_decr))
done
