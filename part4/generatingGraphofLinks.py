import numpy as np
import json

graph = {}


def connectingLinks(connected):
    global graph
    for item in connected:
        for item2 in connected:
            if item != item2:
                try:
                    graph[item][item2] = 1
                except KeyError:
                    graph[item] = {item2: 1}


def preProcessing():
    global graph
    for key, value in graph.items():
        for key2, value2 in value.items():
            graph[key][key2] = graph[key][key2] / len(value)


connected = []

p = 0
with open("../data-00001") as file:
    for line in file:
        if line != "\n":
            parts = line.split()
            title = parts[0]
            if p == 500:
                break
            if title == "URL":
                url = parts[1]
                connectingLinks(connected)
                connected = []
                p += 1

            if title == "TOKEN":
                word = parts[1]
                connected.append(word)


preProcessing()

jsonFile = open('graph.json', 'w')
jsonFile.write(json.dumps(graph, indent=5))
jsonFile.close()