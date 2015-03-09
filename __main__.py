#!/usr/bin/env python3
# Python 3 Script for automatic numbering of lines
#
# Thibault Clerice, @Ponteineptique

import sys
from lxml import etree
import re

regexp = re.compile("(?P<before>[a-zA-Z]+){0,1}(?P<line>[0-9]+){1}(?P<after>[a-zA-Z]+){0,1}")

inputFile = sys.argv[1]

if len(sys.argv) == 3:
    outputFile = sys.argv[2]
else:
    outputFile = inputFile.split(".")
    outputFile = ".".join(outputFile[0:len(outputFile)-1] + ["transformed"] + [outputFile[-1]])

with open(inputFile) as f:
    xml = etree.parse(f)

    lgs = xml.findall(".//tei:*[tei:l]", {"tei": "http://www.tei-c.org/ns/1.0"})
    for x in range(0, len(lgs)):
        lines = lgs[x].findall(".//tei:l", {"tei": "http://www.tei-c.org/ns/1.0"})
        if lines[0].get("n") is None:
            lines[0].set("n", "1")
        for y in range(0, len(lines)):
            l = lines[y]
            if l.get("n"):
                pass
            else:
                match = regexp.match(lines[y-1].get("n")).groupdict()
                n = int(match["line"]) + 1

                if not match["before"]:
                    match["before"] = ""

                if not match["after"]:
                    match["after"] = ""

                n = "{0}{1}{2}".format(match["before"], n, match["after"])
                l.set("n", n)

    with open(outputFile, "wb") as ff:
        xml.write(ff, encoding="utf-8")
