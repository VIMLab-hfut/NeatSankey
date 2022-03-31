import os

os.getcwd()
path = r"D:/Project/Competition/SankeyPaper/realization/UserData/raw"
os.chdir(path)

osWalkResult = []
for i in os.walk(path):
    osWalkResult.append(i)

putInUse = [
    "04EfHMvU.txt",
    "0wMz3Fk6.txt",
    "5c7S6Rdf.txt",
    "6qBNfjDJ.txt",
    "85Tl04oV.txt",
    "aDhy6973.txt",
    "akw6Rioq.txt",
    "aMwFj20e.txt",
    "bjyDhtuM.txt",
    "DBe8OJPY.txt",
    "dW7ylAFr.txt",
    "GwiqYad2.txt",
    "j3cThA9B.txt",
    "Kl7PX35A.txt",
    "KwQoxzk1.txt",
    "lGAtdEYq.txt",
    "MEo9HqFa.txt",
    "MK42izyJ.txt",
    "Na8MHXCy.txt",
    "nVM4uNjD.txt",
    "Oj6Kl4QY.txt",
    "PLVR0OG2.txt",
    "RO1ga8k9.txt",
    "rxdUSz2l.txt",
    "ulvwQEz7.txt",
    "vt4fgaKD.txt",
    "xbqshZDt.txt",
    "YSOfowex.txt",
    "z6ZPGdyX.txt",
    "ZLYR4hvq.txt"
]

files = osWalkResult[0][2]

# for i in files:
# with open('./UserData/0wMz3Fk6.txt', "r", encoding='gbk') as f:
# with open('./UserData/0wMz3Fk6.txt', "r", encoding='utf8') as f:

"""
1-> M1: City of Oakland Budget Sankey Particles
2-> M2: ilp_case_result
3-> M3: product_2
4-> M4: rCharts Examples Sankey Particles
5-> M5: us-energy-consumption
"""
Answer = {
    "1": ["2", "3", "1"],
    "2": ["1", "2", "1"],
    "3": ["1", "4", "2"],
    "4": ["2", "3", "1"],
    "5": ["3", "3", "1"]
}

"""
keys:
    1: Sugiyama
    2: ILP
    3: NEWMethod
values: 
    1: City of Oakland Budget Sankey Particles
    2: ilp_case_result
    3: product_2
    4: rCharts Examples Sankey Particles
    5: us-energy-consumption
"""
# NumsCounting = {
#     "1": {
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "5": 0
#     }, "2": {
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "5": 0
#     }, "3": {
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "5": 0
#     }
# }

# accuracy
# CorrectNumsCounting = {
#     "1": {
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "5": 0
#     }, "2": {
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "5": 0
#     }, "3": {
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "5": 0
#     }
# }

# timecost
# TimecostCounting = {
#     "1": {
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "5": 0
#     }, "2": {
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "5": 0
#     }, "3": {
#         "1": 0,
#         "2": 0,
#         "3": 0,
#         "4": 0,
#         "5": 0
#     }
# }
"""
key:
    1: algorithm Sugiyama
    2: algorithm ILP
    3: algorithm NEWMethod
value:
    1: Task 1,
    2: Task 2,
    3: Task 3
"""
NumsCounting = {
    "1": {
        "1": 0,
        "2": 0,
        "3": 0
    },
    "2": {
        "1": 0,
        "2": 0,
        "3": 0
    },
    "3": {
        "1": 0,
        "2": 0,
        "3": 0
    }
}

CorrectNumsCounting = {
    "1": {
        "1": 0,
        "2": 0,
        "3": 0
    },
    "2": {
        "1": 0,
        "2": 0,
        "3": 0
    },
    "3": {
        "1": 0,
        "2": 0,
        "3": 0
    }
}

TimecostCounting = {
    "1": {
        "1": 0,
        "2": 0,
        "3": 0
    },
    "2": {
        "1": 0,
        "2": 0,
        "3": 0
    },
    "3": {
        "1": 0,
        "2": 0,
        "3": 0
    }
}

# n = open(path + "/processingResult/usefulDetecting.csv", "w+", encoding="utf8")
# n = open(path + "/processingResult/ILPCorrectPercent.csv", "w+", encoding="utf8")
# n = open(path + "/processingResult/sugiyamaCorrectPercent.csv", "w+", encoding="utf8")
# n = open(path + "/processingResult/NEWMethodTimecost.csv", "w+", encoding="utf8")
# n = open(path + "/processingResult/ILPTimecost.csv", "w+", encoding="utf8")
# n = open(path + "/processingResult/sugiyamaTimecost.csv", "w+", encoding="utf8")
# n.write("name,age,major,sex,T1,T2,T3\n")

sugiyamaMaxAccuracy = {"1": 0, "2": 0, "3": 0}
ILPMaxAccuracy = {"1": 0, "2": 0, "3": 0}
NeatSankeyMaxAccuracy = {"1": 0, "2": 0, "3": 0}
sugiyamaMinAccuracy = {"1": 999999999, "2": 999999999, "3": 999999999}
ILPMinAccuracy = {"1": 999999999, "2": 999999999, "3": 999999999}
NeatSankeyMinAccuracy = {"1": 999999999, "2": 999999999, "3": 999999999}

sugiyamaMaxTimecost = {"1": 0, "2": 0, "3": 0}
ILPMaxTimecost = {"1": 0, "2": 0, "3": 0}
NeatSankeyMaxTimecost = {"1": 0, "2": 0, "3": 0}
sugiyamaMinTimecost = {"1": 999999999, "2": 999999999, "3": 999999999}
ILPMinTimecost = {"1": 999999999, "2": 999999999, "3": 999999999}
NeatSankeyMinTimecost = {"1": 999999999, "2": 999999999, "3": 999999999}

SUS = {"Q"+str(_): 0 for _ in range(1, 11)}

STimer = 0

for m in files:
    # if m not in putInUse:
    #     continue
    # STimer += 1
    with open(path + "/" + m, "r", encoding="utf8") as f:
        fileContent = f.read()

    print("---------------------------")
    print(m)

    content = fileContent.split("\n")

    currentResult = {}
    for i in content:
        currentSingleSurveyResult = i.split(": ")
        if currentSingleSurveyResult[0] == "" and len(currentSingleSurveyResult) == 1:
            continue
        currentResult[currentSingleSurveyResult[0]] = currentSingleSurveyResult[1]

    # if "计" not in currentResult["major"][0]:
    #     continue
    STimer += 1

    for i in range(1, 11):
        if i % 2 == 0:
            SUS["Q" + str(i)] += 5 - int(currentResult["Q" + str(i)])
        else:
            SUS["Q" + str(i)] += int(currentResult["Q" + str(i)]) - 1

    realResult = []
    keyResult = []

    # for i in currentResult['questionOrder'].split(';'):
    #     # print(i.split(","))
    #     if i == "":
    #         continue
    #
    #     currentProblemDetail = i.split(",")
    #
    #     value = 0
    #     for t in currentProblemDetail:
    #         if 'AL' == t.split(':')[0]:
    #             value += (int(t.split(':')[1]) - 1) * 15
    #         if 'MA' == t.split(':')[0]:
    #             value += (int(t.split(':')[1]) - 1) * 3
    #         if 'PR' == t.split(':')[0]:
    #             value += int(t.split(':')[1])
    #
    #     if value == 46:
    #         print(i)
    #
    #     # print("Test" + str(value))
    #     realResult.append("Test" + str(value + 1))
    #     keyResult.append(i)

    # print(realResult)
    # print(len(realResult))

    for i in range(1, 46):
        realResult.append("Test" + str(i + 1))
        keyResult.append(
            "AL:" + str((i - 1) // 15 + 1) + ",MA:" + str((i - 1) % 15 // 3 + 1) + ",PR:" + str((i - 1) % 3 + 1))

    resultBasedOrder = {}
    for i in realResult:
        resultBasedOrder[keyResult[realResult.index(i)].replace(",", "").replace(":", "")] = {
            "Timecost": currentResult[i + "Timecost"],
            "Choice": currentResult[i + "Choice"]
        }

    currentUserTimecostCounting = {
        "1": {
            "1": 0,
            "2": 0,
            "3": 0
        },
        "2": {
            "1": 0,
            "2": 0,
            "3": 0
        },
        "3": {
            "1": 0,
            "2": 0,
            "3": 0
        }
    }
    currentUserCorrectNumsCounting = {
        "1": {
            "1": 0,
            "2": 0,
            "3": 0
        },
        "2": {
            "1": 0,
            "2": 0,
            "3": 0
        },
        "3": {
            "1": 0,
            "2": 0,
            "3": 0
        }
    }

    for i in list(resultBasedOrder.keys()):
        NumsCounting[i[2]][i[8]] += 1

        CorrectNumsCounting[i[2]][i[8]] += 1 if Answer[i[5]][int(i[8]) - 1] == resultBasedOrder[i]["Choice"] else 0
        currentUserCorrectNumsCounting[i[2]][i[8]] += 1 if Answer[i[5]][int(i[8]) - 1] == resultBasedOrder[i][
            "Choice"] else 0

        TimecostCounting[i[2]][i[8]] += int(resultBasedOrder[i]["Timecost"])
        currentUserTimecostCounting[i[2]][i[8]] += int(resultBasedOrder[i]["Timecost"])

    sugiyamaMaxAccuracy["1"] = currentUserCorrectNumsCounting["1"]["1"] / 5 if sugiyamaMaxAccuracy["1"] < currentUserCorrectNumsCounting["1"]["1"] / 5 else sugiyamaMaxAccuracy["1"]
    sugiyamaMaxAccuracy["2"] = currentUserCorrectNumsCounting["1"]["2"] / 5 if sugiyamaMaxAccuracy["2"] < currentUserCorrectNumsCounting["1"]["2"] / 5 else sugiyamaMaxAccuracy["2"]
    sugiyamaMaxAccuracy["3"] = currentUserCorrectNumsCounting["1"]["3"] / 5 if sugiyamaMaxAccuracy["3"] < currentUserCorrectNumsCounting["1"]["3"] / 5 else sugiyamaMaxAccuracy["3"]
    ILPMaxAccuracy["1"] = currentUserCorrectNumsCounting["2"]["1"] / 5 if ILPMaxAccuracy["1"] < currentUserCorrectNumsCounting["2"]["1"] / 5 else ILPMaxAccuracy["1"]
    ILPMaxAccuracy["2"] = currentUserCorrectNumsCounting["2"]["2"] / 5 if ILPMaxAccuracy["2"] < currentUserCorrectNumsCounting["2"]["2"] / 5 else ILPMaxAccuracy["2"]
    ILPMaxAccuracy["3"] = currentUserCorrectNumsCounting["2"]["3"] / 5 if ILPMaxAccuracy["3"] < currentUserCorrectNumsCounting["2"]["3"] / 5 else ILPMaxAccuracy["3"]
    NeatSankeyMaxAccuracy["1"] = currentUserCorrectNumsCounting["3"]["1"] / 5 if NeatSankeyMaxAccuracy["1"] < currentUserCorrectNumsCounting["3"]["1"] / 5 else NeatSankeyMaxAccuracy["1"]
    NeatSankeyMaxAccuracy["2"] = currentUserCorrectNumsCounting["3"]["2"] / 5 if NeatSankeyMaxAccuracy["2"] < currentUserCorrectNumsCounting["3"]["2"] / 5 else NeatSankeyMaxAccuracy["2"]
    NeatSankeyMaxAccuracy["3"] = currentUserCorrectNumsCounting["3"]["3"] / 5 if NeatSankeyMaxAccuracy["3"] < currentUserCorrectNumsCounting["3"]["3"] / 5 else NeatSankeyMaxAccuracy["3"]
    
    sugiyamaMinAccuracy["1"] = currentUserCorrectNumsCounting["1"]["1"] / 5 if sugiyamaMinAccuracy["1"] > currentUserCorrectNumsCounting["1"]["1"] / 5 else sugiyamaMinAccuracy["1"]
    sugiyamaMinAccuracy["2"] = currentUserCorrectNumsCounting["1"]["2"] / 5 if sugiyamaMinAccuracy["2"] > currentUserCorrectNumsCounting["1"]["2"] / 5 else sugiyamaMinAccuracy["2"]
    sugiyamaMinAccuracy["3"] = currentUserCorrectNumsCounting["1"]["3"] / 5 if sugiyamaMinAccuracy["3"] > currentUserCorrectNumsCounting["1"]["3"] / 5 else sugiyamaMinAccuracy["3"]
    ILPMinAccuracy["1"] = currentUserCorrectNumsCounting["2"]["1"] / 5 if ILPMinAccuracy["1"] > currentUserCorrectNumsCounting["2"]["1"] / 5 else ILPMinAccuracy["1"]
    ILPMinAccuracy["2"] = currentUserCorrectNumsCounting["2"]["2"] / 5 if ILPMinAccuracy["2"] > currentUserCorrectNumsCounting["2"]["2"] / 5 else ILPMinAccuracy["2"]
    ILPMinAccuracy["3"] = currentUserCorrectNumsCounting["2"]["3"] / 5 if ILPMinAccuracy["3"] > currentUserCorrectNumsCounting["2"]["3"] / 5 else ILPMinAccuracy["3"]
    NeatSankeyMinAccuracy["1"] = currentUserCorrectNumsCounting["3"]["1"] / 5 if NeatSankeyMinAccuracy["1"] > currentUserCorrectNumsCounting["3"]["1"] / 5 else NeatSankeyMinAccuracy["1"]
    NeatSankeyMinAccuracy["2"] = currentUserCorrectNumsCounting["3"]["2"] / 5 if NeatSankeyMinAccuracy["2"] > currentUserCorrectNumsCounting["3"]["2"] / 5 else NeatSankeyMinAccuracy["2"]
    NeatSankeyMinAccuracy["3"] = currentUserCorrectNumsCounting["3"]["3"] / 5 if NeatSankeyMinAccuracy["3"] > currentUserCorrectNumsCounting["3"]["3"] / 5 else NeatSankeyMinAccuracy["3"]
    
    sugiyamaMaxTimecost["1"] = currentUserTimecostCounting["1"]["1"] / 5 if sugiyamaMaxTimecost["1"] < currentUserTimecostCounting["1"]["1"] / 5 else sugiyamaMaxTimecost["1"]
    sugiyamaMaxTimecost["2"] = currentUserTimecostCounting["1"]["2"] / 5 if sugiyamaMaxTimecost["2"] < currentUserTimecostCounting["1"]["2"] / 5 else sugiyamaMaxTimecost["2"]
    sugiyamaMaxTimecost["3"] = currentUserTimecostCounting["1"]["3"] / 5 if sugiyamaMaxTimecost["3"] < currentUserTimecostCounting["1"]["3"] / 5 else sugiyamaMaxTimecost["3"]
    ILPMaxTimecost["1"] = currentUserTimecostCounting["2"]["1"] / 5 if ILPMaxTimecost["1"] < currentUserTimecostCounting["2"]["1"] / 5 else ILPMaxTimecost["1"]
    ILPMaxTimecost["2"] = currentUserTimecostCounting["2"]["2"] / 5 if ILPMaxTimecost["2"] < currentUserTimecostCounting["2"]["2"] / 5 else ILPMaxTimecost["2"]
    ILPMaxTimecost["3"] = currentUserTimecostCounting["2"]["3"] / 5 if ILPMaxTimecost["3"] < currentUserTimecostCounting["2"]["3"] / 5 else ILPMaxTimecost["3"]
    NeatSankeyMaxTimecost["1"] = currentUserTimecostCounting["3"]["1"] / 5 if NeatSankeyMaxTimecost["1"] < currentUserTimecostCounting["3"]["1"] / 5 else NeatSankeyMaxTimecost["1"]
    NeatSankeyMaxTimecost["2"] = currentUserTimecostCounting["3"]["2"] / 5 if NeatSankeyMaxTimecost["2"] < currentUserTimecostCounting["3"]["2"] / 5 else NeatSankeyMaxTimecost["2"]
    NeatSankeyMaxTimecost["3"] = currentUserTimecostCounting["3"]["3"] / 5 if NeatSankeyMaxTimecost["3"] < currentUserTimecostCounting["3"]["3"] / 5 else NeatSankeyMaxTimecost["3"]
    
    sugiyamaMinTimecost["1"] = currentUserTimecostCounting["1"]["1"] / 5 if sugiyamaMinTimecost["1"] > currentUserTimecostCounting["1"]["1"] / 5 else sugiyamaMinTimecost["1"]
    sugiyamaMinTimecost["2"] = currentUserTimecostCounting["1"]["2"] / 5 if sugiyamaMinTimecost["2"] > currentUserTimecostCounting["1"]["2"] / 5 else sugiyamaMinTimecost["2"]
    sugiyamaMinTimecost["3"] = currentUserTimecostCounting["1"]["3"] / 5 if sugiyamaMinTimecost["3"] > currentUserTimecostCounting["1"]["3"] / 5 else sugiyamaMinTimecost["3"]
    ILPMinTimecost["1"] = currentUserTimecostCounting["2"]["1"] / 5 if ILPMinTimecost["1"] > currentUserTimecostCounting["2"]["1"] / 5 else ILPMinTimecost["1"]
    ILPMinTimecost["2"] = currentUserTimecostCounting["2"]["2"] / 5 if ILPMinTimecost["2"] > currentUserTimecostCounting["2"]["2"] / 5 else ILPMinTimecost["2"]
    ILPMinTimecost["3"] = currentUserTimecostCounting["2"]["3"] / 5 if ILPMinTimecost["3"] > currentUserTimecostCounting["2"]["3"] / 5 else ILPMinTimecost["3"]
    NeatSankeyMinTimecost["1"] = currentUserTimecostCounting["3"]["1"] / 5 if NeatSankeyMinTimecost["1"] > currentUserTimecostCounting["3"]["1"] / 5 else NeatSankeyMinTimecost["1"]
    NeatSankeyMinTimecost["2"] = currentUserTimecostCounting["3"]["2"] / 5 if NeatSankeyMinTimecost["2"] > currentUserTimecostCounting["3"]["2"] / 5 else NeatSankeyMinTimecost["2"]
    NeatSankeyMinTimecost["3"] = currentUserTimecostCounting["3"]["3"] / 5 if NeatSankeyMinTimecost["3"] > currentUserTimecostCounting["3"]["3"] / 5 else NeatSankeyMinTimecost["3"]

    # n.write(m +
    #         "," + currentResult["age"] +
    #         "," + currentResult["major"] +
    #         "," + currentResult["sex"] +
    #         "," + str(currentUserCorrectNumsCounting["2"]["1"] / 5) +
    #         "," + str(currentUserCorrectNumsCounting["2"]["2"] / 5) +
    #         "," + str(currentUserCorrectNumsCounting["2"]["3"] / 5) + "\n"
    #         )

    print("processing over")


# n.close()

# finding that the number of total questions is 102 for every problem
def calc(targetDict, processingSource, orderNum):
    for i in range(3):
        targetDict[i] = processingSource[str(orderNum)][str(i + 1)] / 102


# SugiyamaCorrectPercent = {}
# calc(SugiyamaCorrectPercent, CorrectNumsCounting, 1)
# SugiyamaAverageTimecost = {}
# calc(SugiyamaAverageTimecost, TimecostCounting, 1)
#
# ILPCorrectPercent = {}
# calc(ILPCorrectPercent, CorrectNumsCounting, 2)
# ILPAverageTimecost = {}
# calc(ILPAverageTimecost, TimecostCounting, 2)
#
# NEWMethodCorrectPercent = {}
# calc(NEWMethodCorrectPercent, CorrectNumsCounting, 3)
# NEWMethodAverageTimecost = {}
# calc(NEWMethodAverageTimecost, TimecostCounting, 3)

print(SUS)

totalS = 0
UsabilityS = 0
LearnabilityS = 0
for i in range(1, 11):
    if i == 4 or i == 10:
        LearnabilityS += SUS["Q" + str(i)]
    else:
        UsabilityS += SUS["Q" + str(i)]
    totalS += SUS["Q" + str(i)]

print("totalS: " + str(totalS * 2.5 / STimer))
print("UsabilityS: " + str(UsabilityS * 3.125 / STimer))
print("LearnabilityS: " + str(LearnabilityS * 12.5 / STimer))

