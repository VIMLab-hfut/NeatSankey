import math

# from evaluating.M12.dataset_sugiyama import *
# from evaluating.M12.dataset_ilp import *
# from evaluating.M12.dataset_neatsankey import *
from NeatSankeyNodeOrdering.temp_data import *

# we combine two layers into a metrix which is same as sugiyama
# and then detecting the crossing nums and crossing values


"""
Metrics No.1
"""
def MartrixGenerateWithNums(links, level):
    M = []
    for i in range(len(level) - 1):
        M.append([[0.0 for _ in range(len(level[i + 1]))] for _ in range(len(level[i]))])

    # need to combined the result and level for ilp

    layerStart = 0
    layerEnd = 0
    nodeIndexInStartLayer = 0
    nodeIndexInEndLayer = 0
    value = 0
    for i in links:
        for t in level:
            if i["source"] in [_["name"] for _ in t]:
                layerStart = level.index(t)
                layerEnd = layerStart + 1
                nodeIndexInStartLayer = [_["name"] for _ in level[layerStart]].index(i["source"])
                nodeIndexInEndLayer = [_["name"] for _ in level[layerEnd]].index(i["target"])
                value = float(i["value"])
        M[layerStart][nodeIndexInStartLayer][nodeIndexInEndLayer] = 1
        # M[layerStart][nodeIndexInStartLayer][nodeIndexInEndLayer] = value
    return M


def crossingDetectingNums(A):
    KMi = 0
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            for m in range(0, len(A[0]) - 1):
                for n in range(m + 1, len(A[0])):
                    KMi += A[i][n] * A[j][m]
    return KMi


"""
Metrics No.2
"""
def MartrixGenerateWithValues(links, level, zoom):
    M = []
    for i in range(len(level) - 1):
        M.append([[0.0 for _ in range(len(level[i + 1]))] for _ in range(len(level[i]))])

    # need to combined the result and level for ilp

    layerStart = 0
    layerEnd = 0
    nodeIndexInStartLayer = 0
    nodeIndexInEndLayer = 0
    value = 0
    for i in links:
        for t in level:
            if i["source"] in [_["name"] for _ in t]:
                layerStart = level.index(t)
                layerEnd = layerStart + 1
                nodeIndexInStartLayer = [_["name"] for _ in level[layerStart]].index(i["source"])
                nodeIndexInEndLayer = [_["name"] for _ in level[layerEnd]].index(i["target"])
                value = float(i["value"])
        # M[layerStart][nodeIndexInStartLayer][nodeIndexInEndLayer] = 1
        M[layerStart][nodeIndexInStartLayer][nodeIndexInEndLayer] = value * zoom
    return M

def crossingDetectingWidth(A):
    KMi = 0
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            for m in range(0, len(A[0]) - 1):
                for n in range(m + 1, len(A[0])):
                    if A[i][n] * A[j][m] == 0:
                        continue
                    else:
                        KMi += 1 / math.fabs(A[i][n] - A[j][m]) if A[i][n] - A[j][m] != 0 else 0
    return KMi


if __name__ == "__main__":
    # f = open("output_sugiyama.txt", "w+")
    # f = open("output_ilp.txt", "w+")
    f = open("output_neatsankey.txt", "w+")


    totalKn = 0
    totalKv = 0

    counter = 0

    # processing all the 25 datasets
    while counter < len(result_set):
        f.write("----*----\n")
        f.write("auto-generated-data: " + str(counter) + "\n")

        links = links_set[counter]
        level = level_set[counter]
        result = result_set[counter]

        counter += 1

        for i in range(len(level)):
            for t in range(len(level[i])):
                level[i][t]["sourceSize"] = 0
                level[i][t]["targetSize"] = 0
                for m in range(len(links)):
                    if level[i][t]["name"] == links[m]["source"]:
                        level[i][t]["sourceSize"] += float(links[m]["value"])
                    if level[i][t]["name"] == links[m]['target']:
                        level[i][t]["targetSize"] += float(links[m]["value"])
                level[i][t]["size"] = level[i][t]["sourceSize"] if level[i][t]["sourceSize"] > level[i][t][
                    "targetSize"] else level[i][t]["targetSize"]

        totalSize = 0.0
        for i in range(len(level[0])):
            totalSize += level[0][i]["size"]

        zoom = 60 / totalSize

        for i in range(len(level)):
            for t in range(len(level[i])):
                print(level[i][t])
                print(level_set.index(level))
                level[i][t]["size"] = level[i][t]["size"] * zoom

        real_level = [[] for _ in level]
        for i in range(len(result)):
            for t in result[i]:
                real_level[i].append(level[i][t - 1])

        Mn = MartrixGenerateWithNums(links, real_level)
        Kn = 0
        for i in range(len(Mn)):
            Kn += crossingDetectingNums(Mn[i])
        totalKn += Kn
        f.write("Kn: " + str(Kn) + "\n")

        Kv = 0
        Mv = MartrixGenerateWithValues(links, real_level, zoom)
        for i in range(len(Mv)):
            Kv += crossingDetectingWidth(Mv[i])
        totalKv += Kv
        f.write("Kv: " + str(Kv) + "\n\n")

    # put out the result
    f.write("------------------------\n")
    f.write("total Kn: " + str(totalKn) + "\n")
    f.write("average Kn: " + str(totalKn / len(result_set)) + "\n")
    f.write("total Kv: " + str(totalKv) + "\n")
    f.write("average Kv: " + str(totalKv / len(result_set)) + "\n")
    f.close()
