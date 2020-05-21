#!/bin/bash

if grep -q "Conv2D" mn.py 
then
sudo docker run ml:1
else
#launch other image	
echo "code for another image"
fi
