import json
import pandas as pd
import numpy as np

f = open('graph.json')
graph = json.load(f)

matrix = pd.DataFrame.from_dict(graph, orient='columns')
matrix = matrix.fillna(0)

print(matrix)

