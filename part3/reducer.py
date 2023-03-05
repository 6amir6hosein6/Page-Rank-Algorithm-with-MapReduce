#!/usr/bin/env python
"""reducer.py"""

import sys


def Partitioner(couples, total_couple_count=100):
    for item in sorted(couples, key=lambda x: x[1], reverse=True):
        probability = float(item[1]) / float(total_couple_count)
        print('%s\t%s' % (item[0], str(probability) + "%"))


current_key = None
current_value = 0
key = None

list = []

# input comes from STDIN
count_of_couple = 0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)

    if key == "###COUPLE_COUNT###":
        count_of_couple = int(value)
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

Partitioner(list)
