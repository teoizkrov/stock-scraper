#!/bin/bash
i=0
while [ $i -lt 60 ]; do
d=$(date +"%Y-%m-%d-%H-%M-%S" )
filename="$d.html"
wget -O $filename http://www.wsj.com/mdc/public/page/2_3021-activnnm-actives.html
soup="./tagsoup-1.2.1.jar"
if [ ! -e "$soup" ]
then
	wget http://vrici.lojban.org/~cowan/XML/tagsoup/tagsoup-1.2.1.jar
fi

cvs="$d.csv"
java -jar tagsoup-1.2.1.jar --files $filename
python3 dommy.py "$d.xhtml" 
i=$(( i+1 ))
sleep 1m
done



