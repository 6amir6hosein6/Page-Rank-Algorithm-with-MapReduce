#!/usr/bin/env python3
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    if line != "\n":
        parts = line.split()
        title = parts[0]
        if title == "TOKEN":
            word = parts[1]
            word_count = parts[2]
            print('%s\t%s' % (word, word_count))

