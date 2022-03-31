#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from NodeReordering import *
from ForceDirected import *
import sugiyama_with_cycle

import os

if __name__ == '__main__':
    nameList = [
        "../dataset/RandomDataset/auto-generating-data0.json",
        "../dataset/RandomDataset/auto-generating-data1.json",
        "../dataset/RandomDataset/auto-generating-data2.json",
        "../dataset/RandomDataset/auto-generating-data3.json",
        "../dataset/RandomDataset/auto-generating-data4.json",
        "../dataset/RandomDataset/auto-generating-data5.json",
        "../dataset/RandomDataset/auto-generating-data6.json",
        "../dataset/RandomDataset/auto-generating-data7.json",
        "../dataset/RandomDataset/auto-generating-data8.json",
        "../dataset/RandomDataset/auto-generating-data9.json",
        "../dataset/RandomDataset/auto-generating-data10.json",
        "../dataset/RandomDataset/auto-generating-data11.json",
        "../dataset/RandomDataset/auto-generating-data12.json",
        "../dataset/RandomDataset/auto-generating-data13.json",
        "../dataset/RandomDataset/auto-generating-data14.json",
        "../dataset/RealWorldDataset/City of Oakland Budget Sankey Particles.json",
        # "../dataset/RealWorldDataset/dataFromlisachristina1234ongithub.json",
        "../dataset/RealWorldDataset/nottest.json",
        "../dataset/RealWorldDataset/test-data0.json",
        "../dataset/RealWorldDataset/Energy flows in UK (2050).json",
        "../dataset/RealWorldDataset/rCharts Examples Sankey Particles.json",
        "../dataset/RealWorldDataset/medals.json",
        # "../dataset/RealWorldDataset/product_2.json",
        "../dataset/RealWorldDataset/us-energy-consumption.json",
        "../dataset/RealWorldDataset/holiday_data.json",
        "../dataset/RealWorldDataset/PPC Advertising.json",
        "../dataset/RealWorldDataset/Immigrant Flow for Last Month.json"
    ]

    _links_set = []
    _level_set = []
    _result_set = []

    output = open("output.txt", "w+")

    for file in nameList:
        # 当前edges的顺序与originalData["links"]中的排列顺序完全一致
        # 故需要用到value时直接提取即可<-edge.index((a, b))
        with open(file, "r") as f:
            print(f.name)
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
        G_fin, L_fin = sugiyama_with_cycle.graphCrossMin(G_inv, L_b, edges, originalData.get("links"))
        G_fin, L_fin = graphCrossMin(G_fin, L_fin, edges, originalData.get("links"))

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
                            if t == "Packaging":
                                size = 0.000000001
                            if t == "Refrigeration":
                                size = 0.000000001
                    else:
                        for m in originalData["links"]:
                            if t.split('->')[1] == m['source'] and t.split("->")[2] == m["target"]:
                                size = float(m["value"])
                    level_html[i].append({"name": t, "size": size})

        maxTotalSize = max([sum([level_html[i][j]['size']]) for i in range(len(level_html)) for j in range(len(level_html[i]))])
        zoom = 40 / maxTotalSize

        for layer in level_html:
            for item in layer:
                item['size'] *= zoom

        for item in originalData["links"]:
            item['value'] = float(item['value']) * zoom

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

        # originalLevel = [[{"name": "Total", "size": 0.6498581442492419}], [{"name": "Human rights", "size": 0.3075740969932389}, {"name": "Environment", "size": 0.3422840472560037}], [{"name": "Refrigeration", "size": 0.05}, {"name": "Packaging", "size": 0.05}, {"name": "Child labour", "size": 0.04106412026458331}, {"name": "Forced labour", "size": 0.03654585906424446}, {"name": "Health safety", "size": 0.034543532784361106}, {"name": "Access to water", "size": 0.03402066593606667}, {"name": "Freedom of association", "size": 0.03205715239416665}, {"name": "Access to land", "size": 0.03150222098940557}, {"name": "Sufficient wage", "size": 0.028777675722733324}, {"name": "Equal rights migrants", "size": 0.02711466451194445}, {"name": "Discrimination", "size": 0.021121776335983326}, {"name": "Working hours", "size": 0.02082642898974996}, {"name": "Land use", "size": 0.32322870366987}, {"name": "Climate change", "size": 0.011288615741441285}, {"name": "Harmful substances", "size": 0.006042755424956563}, {"name": "Water use", "size": 0.0014834526904470278}, {"name": "Resource depletion", "size": 0.0002405197292887633}], [{"name": "Coconut oil (Organic)", "size": 0.028416608079611102}, {"name": "Vegetables (Organic)", "size": 0.02806193212641737}, {"name": "Cane sugar (Organic)", "size": 0.03220918154120758}, {"name": "Hazelnuts (Organic)", "size": 0.08779767433284562}, {"name": "Cocoa mass (Organic)", "size": 0.22049875020332785}, {"name": "Cocoa butter (Organic)", "size": 0.25287399796583293}]]

        for i in range(len(nodesPositionInfo)):
            for t in range(len(nodesPositionInfo[i])):
                nodesPositionInfo[i][t]["name"] = nodesPositionInfo[i][t]["node"]
                del nodesPositionInfo[i][t]["node"]

        for i in range(len(nodesPositionInfo)):
            for t in range(len(nodesPositionInfo[i])):
                # for m in range(len(originalLevel[i])):
                #     if nodesPositionInfo[i][t]["name"] == originalLevel[i][m]["name"]:
                #         nodesPositionInfo[i][t]["size"] = originalLevel[i][m]["size"]
                del nodesPositionInfo[i][t]["deltaX"]
                del nodesPositionInfo[i][t]["deltaY"]

        finalResult = [[t for t in range(1, len(level_html[i]) + 1)] for i in range(len(level_html))]

        _links_set.append(links_html)
        _level_set.append(nodesPositionInfo)
        _result_set.append(finalResult)

        output.write(
            "----*----\n"
            "fileName: " + file + "\n\n"
            "let links = " + json.dumps(links_html) + "\n\n//nodesPositionInfo:\n" +
            "let level = " + json.dumps(nodesPositionInfo) + "\n\n" +
            "let result = " + json.dumps(finalResult) + "\n\n//original_level\n" +
            "//let level_html = " + json.dumps(level_html) + "\n"
        )

    # output.write()
    output.close()
    print("success!")

    with open("temp_data.py", "w+") as f:
        f.write("links_set = [" + '\n')
        for i in _links_set:
            f.write("\t" + json.dumps(i) + ',\n')
        f.write("]" + '\n\n' + "level_set = [" + "\n")
        for i in _level_set:
            f.write("\t" + json.dumps(i) + ",\n")
        f.write("]" + '\n\n' + "result_set = [" + "\n")
        for i in _result_set:
            f.write("\t" + json.dumps(i) + ",\n")
        f.write("]" + '\n')
