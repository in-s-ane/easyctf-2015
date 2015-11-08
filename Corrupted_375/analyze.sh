#!/bin/bash

/bin/ls EXTRACTED* | while read out; do if [[ `file $out` == *": data" ]]; then rm -f $out; fi; done
