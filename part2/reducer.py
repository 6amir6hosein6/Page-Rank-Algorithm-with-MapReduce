#!/usr/bin/env python
"""reducer.py"""

import sys
import numpy as np


def Partitioner(words_frequency, total_documents):
    for item in words_frequency:
        print('%s\t%s' % (item[0], np.log(total_documents / (item[1] + 1))))


current_key = None
current_value = 0
key = None

list = []

# input comes from STDIN
total_number_of_documents = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)

    if key == "###TOTAL_NUMBER_OF_DOCUMENTS###":
        total_number_of_documents = int(value)
        continue

    # convert value (currently a string) to int
    try:
        value = int(value)
    except ValueError:
        # value was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: key) before it is passed to the reducer
    if current_key == key:
        current_value += value
    else:
        if current_key:
            # write result to STDOUT
            list.append([current_key, current_value])
            # print('%s\t%s' % (current_key, current_value))
        current_value = value
        current_key = key

# do not forget to output the last key if needed!
if current_key == key:
    list.append([current_key, current_value])
    # print('%s\t%s' % (current_key, current_value))

Partitioner(list, total_number_of_documents)
