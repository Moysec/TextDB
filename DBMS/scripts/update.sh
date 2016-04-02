#! /usr/bin/env sh

DBNAME=$1
shift;
wantedfield=$1
shift;
data=$1
shift;

field=`awk -v wanted="$wantedfield" 'BEGIN{ FS="$"; } 
{ for(fn=1;fn<=NF;fn++) {if($fn == wanted) print fn;}; exit; }
         ' $MODELPATH/$DBNAME".sch"`
fields=`sed  "s/[$]/ /g" $MODELPATH/$DBNAME".sch"`
matched_lines=`awk -v field=$field 'BEGIN{FS="$";} {print $field;}' $DBPATH/$DBNAME".db" | sed -n "/$data/="`

line_decr=0
for line_num in $matched_lines
do
    matched_line=`awk -v new_line_num=$((line_num - line_decr)) 'NR==new_line_num' $DBPATH/$DBNAME".db" | sed "s/[$]/ /g"` 
    sed -i "$((line_num - line_decr))d" $DBPATH/$DBNAME".db"
    line_decr=$((line_decr + 1))
    for new_data in $@
    do
        new_data=`echo $new_data | sed "s/[:]/ /g"`
        new_data_field=`echo $new_data | awk '{print $1}'`
        new_data_data=`echo $new_data | awk '{print $2}'`
        field=`awk -v wanted=$new_data_field 'BEGIN {FS="$" } {for(fn=1;fn<=NF;fn++) {if($fn == wanted) print fn;}; exit; }' $MODELPATH/$DBNAME".sch"`       
        matched_line=`echo $matched_line | awk -v new_data=$new_data_data -v field=$field '{$field=new_data; print;}'`
    done
    echo $matched_line | sed 's/[ ]/\$/g' >> $DBPATH/$DBNAME".db"
done
