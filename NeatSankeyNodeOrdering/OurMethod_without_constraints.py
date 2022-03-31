#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from NodeReordering_without_constraints import *
from ForceDirected_without_constraints import *

if __name__ == '__main__':
    # 当前edges的顺序与originalData["links"]中的排列顺序完全一致
    # 故需要用到value时直接提取即可<-edge.index((a, b))
    # with open("./dataset/product_2.json", mode="r") as f:
    # with open("./dataset/product_2.json", mode="r") as f:
    # with open("./dataset/product_2.json", mode="r") as f:
    with open("./dataset/product_2.json", mode="r") as f:
    # with open("./test-data0.json", mode="r") as f:

        originalData = json.load(f)
    edges = []
    for i in originalData.get("links"):
        edges.append((i["source"], i["target"]))

    G = graphFromEdges(edges)  # 完成对原始边集的访问并生成以顶点为键，以出入边为键值的字典对象为值的新字典：N
    S = cycleAnalysis(G)  # 消除环图
    # printGraph(G)  # 打印G

    G_inv = invertBackEdges(G, S)  # inverted edges are only for level assignment
    L = levelAssignment(G_inv)  # figure out the level and the nodes on the level, L contains the level info
    # print(L)

    # search for the best situation which the most important part
    G_inv, L_b = getInBetweenNodes(G_inv, L)  # add virtual nodes to prevent links crossing levels
    # print(L_b)

    G_fin, L_fin = graphCrossMin(G_inv, L_b, edges, originalData.get("links"))

    links_html = []
    level_html = [[] for _ in range(len(L_fin))]
    for i in range(len(L_fin)):
        size = 0
        if i == len(L_fin) - 1:
            for t in L_fin[i]:
                size = 0
                for m in originalData["links"]:
                    if m['target'] == t:
                        size += float(m['value'])
                level_html[i].append({"name": t, "size": size})
        else:
            for t in L_fin[i]:
                size = 0
                if len(t.split('->')) == 1:
                    for m in originalData["links"]:
                        if m['source'] == t:
                            size += float(m['value'])
                else:
                    for m in originalData["links"]:
                        if t.split('->')[1] == m['source'] and t.split("->")[2] == m["target"]:
                            size = float(m["value"])
                level_html[i].append({"name": t, "size": size})

    # generate the "links" list which we need for html file
    # in this part, we only analyze the "out" part in G_fin
    # and when we meet the dummy node, we just need to
    # search for the original link
    # we use the combination of part[2] for source name
    # and part[3] for target name in dummy node name
    # such as "dummy->Livestock and Manure->Methane->V2"
    # will be changed into Livestock and Manure, Methane
    for i in list(G_fin.keys()):
        splitResult = i.split('->')
        if len(splitResult) == 1:
            # the 'source node' is regular node, not dummy
            for t in G_fin[i]['out']:
                temp = t.split("->")
                if len(temp) == 1:
                    # the 'target node' is also regular node
                    for m in originalData['links']:
                        if m['source'] == i and m['target'] == t:
                            links_html.append({'source': i, 'target': t, 'value': m['value']})
                else:
                    # attention! 'target node' is dummy node
                    for m in originalData['links']:
                        if m['source'] == i and m['target'] == temp[2]:
                            links_html.append({'source': i, 'target': t, 'value': m['value']})

        else:
            # it's dummy node and there is only one link in its 'out' list
            for t in G_fin[i]['out']:
                for m in originalData['links']:
                    if m['source'] == splitResult[1] and m['target'] == splitResult[2]:
                        links_html.append({'source': i, 'target': t, 'value': m['value']})

    nodesPositionInfo = FR(L_fin, G_fin, links_html, level_html)


    originalLevel = [[{'name': 'Agriculture', 'size': 13.8}, {'name': 'Waste', 'size': 3.2}, {'name': 'Energy', 'size': 65.6}, {'name': 'Industrial Processes', 'size': 5.1}, {'name': 'Land Use Change', 'size': 12.200000000000001}], [{'name': 'Rice Cultivation', 'size': 1.5}, {'name': 'Other Agriculture', 'size': 1.7}, {'name': 'Landfills', 'size': 1.7}, {'name': 'Livestock and Manure', 'size': 5.3999999999999995}, {'name': 'Waste water - Other Waste', 'size': 1.5}, {'name': 'Agriculture Soils', 'size': 5.2}, {'name': 'Fugitive Emissions', 'size': 4.5}, {'name': 'Other Fuel Combustion', 'size': 9.1}, {'name': 'Electricity and heat', 'size': 23.0}, {'name': 'dummy->Industrial Processes->Chemicals->V1', 'size': 1.4}, {'name': 'Industry', 'size': 14.3}, {'name': 'dummy->Industrial Processes->Cement->V1', 'size': 2.8}, {'name': 'Transportation', 'size': 14.7}, {'name': 'Harvest / Management', 'size': 1.3}, {'name': 'Deforestation', 'size': 10.9}, {'name': 'dummy->Industrial Processes->Other Industry->V1', 'size': 0.5}, {'name': 'dummy->Industrial Processes->Aluminium Non-Ferrous Metals->V1', 'size': 0.4}], [{'name': 'dummy->Rice Cultivation->Methane->V2', 'size': 1.5}, {'name': 'dummy->Other Agriculture->Methane->V2', 'size': 1.4}, {'name': 'dummy->Livestock and Manure->Methane->V2', 'size': 5.1}, {'name': 'dummy->Landfills->Methane->V2', 'size': 1.7}, {'name': 'dummy->Waste water - Other Waste->Methane->V2', 'size': 1.2}, {'name': 'dummy->Other Agriculture->Nitrous Oxide->V2', 'size': 0.3}, {'name': 'dummy->Livestock and Manure->Nitrous Oxide->V2', 'size': 0.3}, {'name': 'dummy->Agriculture Soils->Nitrous Oxide->V2', 'size': 5.2}, {'name': 'dummy->Waste water - Other Waste->Nitrous Oxide->V2', 'size': 0.3}, {'name': 'Coal Mining', 'size': 1.3}, {'name': 'Unallocated Fuel Combustion', 'size': 3.8}, {'name': 'Oil and Gas Processing', 'size': 6.4}, {'name': 'Agricultural Energy Use', 'size': 1.4}, {'name': 'Commercial Buildings', 'size': 6.3}, {'name': 'Residential Buildings', 'size': 10.2}, {'name': 'Machinery', 'size': 1.0}, {'name': 'T and D Losses', 'size': 2.2}, {'name': 'Food and Tobacco', 'size': 1.0}, {'name': 'Iron and Steel', 'size': 4.0}, {'name': 'Pulp - Paper and Printing', 'size': 1.1}, {'name': 'Chemicals', 'size': 4.1}, {'name': 'Cement', 'size': 5.0}, {'name': 'Air', 'size': 1.7}, {'name': 'Rail - Ship and Other Transport', 'size': 2.5}, {'name': 'Road', 'size': 10.5}, {'name': 'dummy->Harvest / Management->Carbon Dioxide->V2', 'size': 1.3}, {'name': 'dummy->Deforestation->Carbon Dioxide->V2', 'size': 10.9}, {'name': 'Other Industry', 'size': 7.0}, {'name': 'Aluminium Non-Ferrous Metals', 'size': 1.2}], [{'name': 'Methane', 'size': 15.3}, {'name': 'Nitrous Oxide', 'size': 6.7}, {'name': 'Carbon Dioxide', 'size': 76.8}, {'name': 'HFCs - PFCs', 'size': 1.1}]]

    for i in range(len(nodesPositionInfo)):
        for t in range(len(nodesPositionInfo[i])):
            nodesPositionInfo[i][t]["name"] = nodesPositionInfo[i][t]["node"]
            del nodesPositionInfo[i][t]["node"]


    for i in range(len(nodesPositionInfo)):
        for t in range(len(nodesPositionInfo[i])):
            for m in range(len(originalLevel[i])):
                if nodesPositionInfo[i][t]["name"] == originalLevel[i][m]["name"]:
                    nodesPositionInfo[i][t]["size"] = originalLevel[i][m]["size"]
            del nodesPositionInfo[i][t]["deltaX"]
            del nodesPositionInfo[i][t]["deltaY"]

# if __name__ == '__main__':
#     layerList = [
#         ['a', 'b', 'c', 'd'],
#         ['1', '2', '3', '4']
#     ]
#     G = {'1': {'in':['c']},
#          '2':{'in':['a', 'c']},
#          '3':{'in':['b', 'd']},
#          '4':{'in':['c', 'd']}
#     }
#     print(barycenterDirectlyCalc(layerList, G))
