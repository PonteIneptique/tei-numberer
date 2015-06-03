#!/usr/bin/env python3
# Python 3 Script for automatic HTMLEntities Conversions
#
# Thibault Clerice, @Ponteineptique

import sys
import html

inputFile = sys.argv[1]

if len(sys.argv) == 3:
    outputFile = sys.argv[2]
else:
    outputFile = inputFile.split(".")
    outputFile = ".".join(outputFile[0:len(outputFile)-1] + ["transformed"] + [outputFile[-1]])

with open(inputFile) as f:
    unescaped = html.unescape(f.read())

    with open(outputFile, "w") as ff:
        ff.write(unescaped)
