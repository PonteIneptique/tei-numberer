#!/usr/bin/env python3
# Python 3 Script for automatic GreekBetaCode
#
# Thibault Clerice, @Ponteineptique

import sys
from lxml import etree
from betacode2uni import beta2unicodeTrie

inputFile = sys.argv[1]

if len(sys.argv) == 3:
    outputFile = sys.argv[2]
else:
    outputFile = inputFile.split(".")
    outputFile = ".".join(outputFile[0:len(outputFile)-1] + ["transformed"] + [outputFile[-1]])

with open(inputFile) as f:
    xml = etree.parse(f)
    converter = beta2unicodeTrie()
    greeks = xml.findall(".//tei:foreign[@lang='greek']", {"tei": "http://www.tei-c.org/ns/1.0"})
    for greek in greeks:
        greek.text, debug = converter.convert(greek.text.upper())
        greek.set("lang", "grc")

    with open(outputFile, "wb") as ff:
        xml.write(ff, encoding="utf-8")
