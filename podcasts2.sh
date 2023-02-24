#!/bin/bash
count=$(xmllint --xpath 'count(//enclosure/@url)' a.xml)
for (( i=1; i<=count; ++i )); do
   echo "$(xmllint --xpath "string((//enclosure/@url)[$i])" a.xml)"
done
