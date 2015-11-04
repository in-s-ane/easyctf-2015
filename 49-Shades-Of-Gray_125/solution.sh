#!/bin/bash

convert shades.png -format %c -depth 8 histogram:info:- | grep -Po '(?<=\().*?(?=\))' > VALUES.txt

# Above command gives us a histogram of all the pixel values.

tr -d ' \t\f' < VALUES.txt > STRIPPED.txt

# Strips the spacesfor easy parsing

for i in `seq 0 255`; do
    if ! cat STRIPPED.txt | grep $i > /dev/null; then
        echo $i
    fi
done;

