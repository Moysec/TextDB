#! /usr/bin/env sh

#take 3 arguments(database name, field and wanted data), and output schema structure in the first line and lines which contain wanted data in the rest of the lines
DBNAME=$1
wantedfield=$2
pattern=$3
#SELECT=`echo $@ | sed "s/[ ]/\$/g"`
field=`awk -v wanted="$wantedfield" 'BEGIN{ FS="$"; } 
{ for(fn=1;fn<=NF;fn++) {if($fn == wanted) print fn;}; exit; }
         ' $MODELPATH/$DBNAME".sch"`
fields=`sed  "s/[$]/ /g" $MODELPATH/$DBNAME".sch"`
echo $fields
matched_lines=`awk -v field=$field 'BEGIN{FS="$";} {print $field;}' $DBPATH/$DBNAME".db" | sed -n "/$pattern/="`
for line_num in $matched_lines
do
    awk -v line_num=$line_num 'NR==line_num' $DBPATH/$DBNAME".db" | sed "s/[$]/ /g"  
done
