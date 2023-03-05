import json
import pandas as pd

f = open('graph.json')
graph = json.load(f)

matrix = pd.DataFrame.from_dict(graph, orient='columns', dtype=None)
matrix = matrix.fillna(0)

nodes_count = len(graph)

PR = [(10000/nodes_count) for i in range(nodes_count)]
PR = pd.Series(PR, index=matrix.columns)

epoch = 100
for i in range(epoch):
    PR = matrix.dot(PR)
    print("Epoch => " + str(i) + "/" + str(epoch))

PR.sort_values(ascending=False).to_csv("final_page_rank.csv", sep='\t', encoding='utf-8')


