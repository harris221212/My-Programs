#! /bin/sh

python podcasts.py $1 tempList.txt
wget -i tempList.txt
rm tempList.txt
