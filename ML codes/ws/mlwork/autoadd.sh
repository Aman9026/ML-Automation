#!/bin/bash
epoch=5
accuracy= python /home/mn.py | tail -50 | head -1 | cut -d " " -f 11 | cut -c3-
while [[ $accuracy -lt 9900 && $epoch -lt 20 ]] 
do 

a=0
a=$(grep -n -e "model.fit(x=x_train,y=y_train, epochs=$epoch)" /home/mn.py |  cut -d ":" -f1)
epoch=`expr $epoch + 5`
#let a++
echo $a
sed -i "${a}s/.*/model.fit(x=x_train,y=y_train, epochs=$epoch)/" mn.py
accuracy= python /home/mn.py | tail -50 | head -1 | cut -d " " -f11 | cut -c3-

done 



#Alternates
#a=$(grep -n -e "model.compile(optimizer='adam'" test |  cut -d ":" -f1)
#echo $a
#sed -i "${a}s/.*/model.compile(optimizer='adamax'/" test

#a=$(grep -n -e "model.compile(optimizer='adam'" test |  cut -d ":" -f1)
#echo $a
#sed -i "${a}s/.*/model.compile(optimizer='nadam'/" test
