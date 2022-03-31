import math


def FR(lvl, Graph, links_html, level_html):
    nodesPositionInfo = defaultPositionCalc(lvl, level_html)
    layerPadding = {i: 448 * i for i in range(len(lvl))}

    nodesPositionInfo = layerInsideFRProgress(lvl, level_html, nodesPositionInfo)

    nodesPositionInfo = layerOutsideFRProgress(lvl, Graph, nodesPositionInfo, level_html, layerPadding)
    # layerPadding = layerFRProgress2(lvl, Graph, layerPadding)

    return nodesPositionInfo


def defaultPositionCalc(lvl, level_html):
    defaultPosition = [[] for _ in range(len(lvl))]

    defaultLayerPadding = 448
    defaultNodeWidth = 36
    defaultNodePadding = 10

    for i in range(len(lvl)):
        layerLength = 0
        for t in range(len(lvl[i])):
            defaultPosition[i].append({
                "node": lvl[i][t],
                "x": defaultLayerPadding * i + defaultLayerPadding / 2,
                "y": level_html[i][t]["size"] + layerLength,
                "deltaX": 0,
                "deltaY": 0
            })
            layerLength += 2 * level_html[i][t]["size"] + defaultNodePadding

    return defaultPosition


def cool(temper, curIter, maxIter):
    return temper * (1.0 - curIter/maxIter)

def initBorder(border, layerNum, layerLength, position, level_html, i):
    # for node in range(layerNum):
    #     minmax = dict()
    #     if node == 0:
    #         minmax['min'] = 0
    #         minmax['max'] = position[i][node + 1]['y'] if node + 1 < layerNum else layerLength
    #     elif node == layerNum - 1:
    #         minmax['min'] = position[i][node - 1]['y'] if node - 1 > -1 else 0
    #         minmax['max'] = layerLength
    #     else:
    #         minmax['min'] = position[i][node - 1]['y']
    #         minmax['max'] = position[i][node + 1]['y']
    #     border[node] = minmax

    gap = min([node["size"] for node in level_html[i]]) / 10

    for node in range(layerNum):
        minmax = dict()
        if node == 0:
            minmax['min'] = 0
            minmax['max'] = 2 * level_html[i][node]['size']
        else:
            minmax['min'] = position[i][node]['y'] - level_html[i][node]['size'] \
                if position[i][node]['y'] - level_html[i][node]['size'] > 0 else 0
            minmax['min'] = minmax['min'] if minmax['min'] > position[i][node - 1]['y'] else position[i][node - 1]['y']
            if minmax['min'] < border[node - 1]['max']:
                newBorder = (minmax['min'] + border[node - 1]['max']) / 2
                minmax['min'] = newBorder + gap
                border[node - 1]['max'] = newBorder - gap
            minmax['max'] = position[i][node]['y'] + level_html[i][node]['size'] \
                if position[i][node]['y'] + level_html[i][node]['size'] < layerLength else layerLength
        border[node] = minmax

def layerInsideFRProgress(lvl, level_html, position):
    # in progress1 inside part, we have two types of force between nodes: fa(d) and fr(d)
    # fa(d) stands for gravitation, while fr(d) stands for the repulsion
    # force between two vertices is fa(d) = d^2 / k if (abs(w1 - w2) / (w1 + w2)) >= w
    # meanwhile, force is fr(d) = -k^2 / d if (abs(w1 - w2) / (w1 + w2)) < w

    # k = C * sqrt(area / number of vertices)
    # C = delta * 1 / (abs((wi - wj) / (wi + wj)))

    # wi and wj both stand for the width their nodes have
    for i in range(len(lvl)):
        # default padding between node in one layer

        # default values
        # nodeWidth = 36


        layerNum = len(lvl[i])
        nodeLength = max([node["size"] for node in level_html[i]])
        layerLength = position[i][-1]["y"] + nodeLength

        temper = layerLength / layerNum
        maxIter = 200

        # hyperparameter is defined here
        w = 0.5
        delta = 10
        Cmax = layerLength / layerNum

        border = dict()
        initBorder(border, layerNum, layerLength, position, level_html, i)

        for curIter in range(maxIter):
            # start the cycle
            for t in range(layerNum):
                # variable t is the pointer which points to node we need to calculate
                for m in range(layerNum):
                    # variable t is the pointer which points to nodes need to be compared
                    if t == m:
                        continue
                    else:
                        wi = level_html[i][t]["size"] * 4
                        wj = level_html[i][m]["size"] * 4
                        deltaW = math.fabs((wi - wj) / (wi + wj))

                        c = Cmax if math.fabs(deltaW) < 0.01 else delta * (1 / deltaW)
                        # 第i层节点最后一个节点的大小+最后一个节点的y值

                        k = c * math.sqrt(layerLength / layerNum)

                        sig = 1.0 if position[i][m]['y'] - position[i][t]['y'] > 0 else -1.0

                        deltaY = math.fabs(position[i][t]['y'] - position[i][m]['y']) \
                            if math.fabs(position[i][t]['y'] - position[i][m]['y']) > 0.01 else 0.01

                        # print(k)

                        # 引力 斥力
                        fd = deltaY * deltaY / k \
                            if deltaW > w \
                            else -k * k / deltaY

                        # print(fd, deltaW, deltaY, k)

                        position[i][t]["deltaY"] = position[i][t]["deltaY"] + sig * fd
            # 当前层每个节点的偏移量确定后则issue
            for t in range(len(lvl[i])):
                position[i][t]["deltaY"] = 0 if not position[i][t]["deltaY"] else \
                    position[i][t]["deltaY"] / math.fabs(position[i][t]["deltaY"]) * \
                                            min(math.fabs(position[i][t]["deltaY"]), temper)
                position[i][t]["y"] += position[i][t]["deltaY"]
                position[i][t]["y"] = min(border[t]['max'],
                                          max(border[t]['min'], position[i][t]["y"] + level_html[i][t]['size']/2))
                position[i][t]["y"] = min(border[t]['max'],
                                          max(border[t]['min'], position[i][t]["y"] - level_html[i][t]['size'] / 2))
                position[i][t]["deltaY"] = 0
                # updateBorder(border, layerNum, layerLength, position, i)

            temper = cool(temper, curIter, maxIter)

    return position

def initOutsideBorder(border, layerNum, layerGap):

    for node in range(layerNum):
        minmax = dict()
        minmax['min'] = node * layerGap
        minmax['max'] = node * layerGap + layerGap
        border[node] = minmax


def layerOutsideFRProgress(lvl, Graph, position, level_html, layerPadding):
    # in progress1 outside part, we  still have two types of force: fa(d) and fr(d)
    # but we recongnize one entire layer as a node in the algorithm, so everything is same
    # fa(d) stands for gravitation, while fr(d) stands for the repulsion
    # force between two vertices is fa(d) = d^2 / k if (abs(w1 - w2) / (w1 + w2)) >= w

    # meanwhile, force is fr(d) = -k^2 / d if (abs(w1 - w2) / (w1 + w2)) < w
    # k = C * sqrt(area / number of vertices)
    # C = delta * 1 / (abs((wi - wj) / (wi + wj)))

    # wi and wj both stand for the width their nodes have
    # for i in range(len(lvl)):
    #     # hyperparameter is defined here
    #     w = 0.5
    #     delta = 1
    #     Cmax = 10
    #
    #     # default values
    #     # nodeWidth = 36
    #
    #     # start the cycle
    #     for t in range(len(lvl)):
    #         # variable t is the pointer which points to node we need to calculate
    #         if i == t:
    #             continue
    #         else:
    #             area = 1380 * 720
    #
    #             wi = 0
    #             for m in range(len(level_html[i])):
    #                 wi += level_html[i][m]["size"] * 4
    #             wj = 0
    #             for m in range(len(level_html[t])):
    #                 wj += level_html[t][m]["size"] * 4
    #
    #             c = Cmax if wi - wj < 0.01 else delta * (1 / math.fabs((wi - wj) / (wi + wj)))
    #
    #             k = c * math.sqrt(area / len(lvl[i]))
    #
    #             fd = (math.fabs(layerPadding[t] - layerPadding[i]) + 36) * (
    #                         math.fabs(layerPadding[t] - layerPadding[i]) + 36) / k \
    #                 if math.fabs(wi - wj) / (wi + wj) > w \
    #                 else -k * k / math.fabs(layerPadding[t] - layerPadding[i]) + 36
    #
    #             layerPadding[i] += layerPadding[i] + fd
    # return layerPadding

    layerNum = len(lvl)
    layerGap = (position[len(lvl) - 1][0]["x"] - position[0][0]["x"]) / (layerNum-1)
    layerLength = position[len(lvl) - 1][-1]["x"] + layerGap

    # default padding between node in one layer

    # default values
    # nodeWidth = 36

    temper = layerLength / layerNum
    maxIter = 200

    # hyperparameter is defined here
    w = 0.5
    delta = 10

    border = dict()
    initOutsideBorder(border, layerNum, layerGap)
    # 计算每层连接的边的总数
    edgeNum = dict()
    for i in range(1, layerNum):
        edgeNum[i - 1] = 0
        for node in lvl[i]:
            edgeNum[i-1] += len(Graph[node]['in'])

    Xgroup = [position[i][0]['x'] for i in range(layerNum)]

    for curIter in range(maxIter):

        deltaXgroup = [0]*layerNum

        for i in range(layerNum-1):
            # 线越多，引力越小
            c = delta * edgeNum[i]
            # 第i层节点最后一个节点的大小+最后一个节点的y值

            k = c * math.sqrt(layerLength / layerNum)

            deltaX = Xgroup[i+1] - Xgroup[i]

            # 引力
            fd = deltaX * deltaX / k

            print(k, fd, deltaX)

            deltaXgroup[i] += fd
            deltaXgroup[i+1] -= fd
        # 当前层每个节点的偏移量确定后则issue
        for i in range(layerNum):
            deltaXgroup[i] = 0 if not deltaXgroup[i] else \
                deltaXgroup[i] / math.fabs(deltaXgroup[i]) * \
                min(math.fabs(deltaXgroup[i]), temper)
            Xgroup[i] += deltaXgroup[i]
            Xgroup[i] = min(border[i]['max'], max(border[i]['min'], Xgroup[i]))

        temper = cool(temper, curIter, maxIter)

    for i in range(layerNum):
        perLayerNum = len(position[i])
        for j in range(perLayerNum):
            position[i][j]['x'] = Xgroup[i]

    return position

#
# def layerFRProgress2(lvl, Graph, currentLayerPadding):
#     # this part, we only change the distance between layers
#
#     # in this part:
#     # f(d) = d^2 / k
#     # k = c * sqrt(area / number of vertices)
#     # c = delta / (number of links between two layers)
#     for i in range(len(lvl) - 1):
#         for t in range(len(lvl) - 1):
#             if i == t:
#                 continue
#
#             linksSum = 0
#             for t in range(len(lvl[i])):
#                 # we just need to count all links in source in first layer or target in second layer
#                 linksSum += len(Graph[lvl[i][t]]["out"])
#
#             delta = 1
#             C = delta / linksSum
#
#             # the total area of the picture
#             area = 1380 * 720
#
#             K = C * math.sqrt(area / len(lvl[i]))
#
#             if i < t:
#                 # if layer t is on the right side of the layer i, then layer t will provide a force toward right
#                 # which will make the posX increase
#                 currentLayerPadding[i] = currentLayerPadding[i] + currentLayerPadding[i] * currentLayerPadding[i] / K
#             else:
#                 # and if layer t is on the left side of the layer i, then layer t will provide a force toward left
#                 # which will make the posX decrease
#                 currentLayerPadding[i] = currentLayerPadding[i] - currentLayerPadding[i] * currentLayerPadding[i] / K
#
#     return currentLayerPadding
