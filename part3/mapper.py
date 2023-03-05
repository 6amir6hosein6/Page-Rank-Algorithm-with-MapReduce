#!/usr/bin/env python3
"""mapper.py"""

import sys
import itertools


def Combiner(links_tokens):
    count_of_all_couples = 0
    for key in links_tokens.keys():
        for pair in itertools.combinations(links_tokens[key], 2):
            count_of_all_couples += 1
            print('%s\t%s' % ("(" + pair[0] + "," + pair[1] + ")", 1))

    print('%s\t%s' % ("###COUPLE_COUNT###", count_of_all_couples))



# input comes from STDIN (standard input)
is_new_url = 0


links_tokens = {}
url = ""

for line in sys.stdin:
    if line != "\n":
        parts = line.split()
        title = parts[0]

        if title == "TOKEN":
            word = parts[1]
            links_tokens[url].append(word)

        if title == "URL":
            url = parts[1]
            links_tokens[url] = []

Combiner(links_tokens)
