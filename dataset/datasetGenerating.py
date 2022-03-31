import json
import random
import time

for fileO in range(1):
    random.seed(time.time())

    #
    totalValue = random.randrange(100, 200)

    # from 0 to (layers)
    layers = 4

    nodesNums = [random.randrange(3, 20) for _ in range(layers)]
    nodes = []
    for i in range(layers):
        layerNodes = []
        for t in range(nodesNums[i]):
            layerNodes.append({"name": "L" + str(i) + "N" + str(t)})
        nodes.append(layerNodes)

    # generate edges
    edges = []
    for i in range(layers - 1):
        # 当前层的值
        value = totalValue
        # 每个节点的值
        nodeVals = []

        # 当前层每个节点的value
        for j in range(nodesNums[i]-1):
            while True:
                curVal = random.randint(1, value)
                if value - curVal >= nodesNums[i]-j-1:
                    break
            nodeVals.append(curVal)
            value -= curVal
        nodeVals.append(value)


        # 对于第 j 个节点
        for j in range(nodesNums[i]):

            # 当前节点的值
            curNodeVal = nodeVals[j]
            links = curNodeVal + 1
            # 该节点所连的边
            while links > curNodeVal:
                links = random.randint(1, nodesNums[i+1])
            # 该节点所连接的节点
            nextNodes = set()
            while len(nextNodes) < links:
                nextNodes.add(random.choice([item["name"] for item in nodes[i+1]]))

            linkVals = []

            # 当前节点每条边的value
            for k in range(links - 1):
                while True:
                    curLinkVal = random.randint(1, curNodeVal)
                    if curNodeVal - curLinkVal >= links-k-1:
                        break
                linkVals.append(curLinkVal)
                curNodeVal -= curLinkVal
            linkVals.append(curNodeVal)

            for k, nextNode in enumerate(nextNodes):
                edges.append(
                    {
                        "source": "L" + str(i) + "N" + str(j),
                        "target": nextNode,
                        "value": linkVals[k]
                    }
                )

    with open("./RandomDataset/auto-generating-data" + str(14) + ".json", mode="w+") as f:
        f.write(
            json.dumps(
                {
                    "nodes": [node for item in nodes for node in item],
                    "links": edges
                }
            )
        )
