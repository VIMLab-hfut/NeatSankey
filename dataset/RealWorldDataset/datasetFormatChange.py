import json

# with open("./dataset/China Provice Party.json") as f:
#     content = json.load(f)
#
# nodes = [{"name": i["name"]} for i in content.get('nodes')]
# links = content.get('links')
#
# for i in range(len(links)):
#     for t in links[i].keys():
#         if t == "value":
#             continue
#         for m in content.get('nodes'):
#             if links[i].get(t) == m['node']:
#                 links[i][t] = m['name']
#
# with open("./dataset/China Provice Party After Processing.json", mode="w") as g:
#     g.write(json.dumps({"nodes": nodes, "links": links}))
# # print({"nodes": nodes, "links": links})

# with open("./dataset/us-energy-consumption.csv") as f:
with open("holiday_data.csv") as f:
    content = f.readlines()

print(content)

nodes = []
links = []

for i in range(len(content)):
    if i == 0:
        continue
    else:
        m = content[i].split(',')
        links.append({"source": m[4], "target": m[5], "value": float(m[2].replace("\n", ""))})
        if m[4] not in nodes:
            nodes.append(m[4])
        if m[5] not in nodes:
            nodes.append(m[5])


results = {"nodes": [], "links": []}

with open("holiday_data.json", mode="w") as f:
    f.write(json.dumps({"nodes": [{"name": i} for i in nodes], "links": links}))

# import random
# result = []
# while len(result) <= int(43*0.3) + 1:
#     temp = int(random.random() * 43)
#     if temp + 1 not in result:
#         result.append(temp + 1)
#
# print(sorted(result))
