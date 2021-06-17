import json

# Opening JSON file
f = open('data.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

calcData = []
for i in data:
    extractData = i["data"]
    minValue = 100000000000
    for s in extractData:
        if (s["year"] == "2020" and s["periodName"] == "March"):
            # calcData.append(i["Area"])
            # index = calcData.index(i["Area"])
            d = {i["Area"]: [("peak", s["value"])]}
            calcData.append(d)
            # calcData[index] = ("peak", s["value"])

        # print(float(s["value"]) >= minValue)
        if(float(s["value"]) <= minValue):
            minValue = float(s["value"])
    for a in calcData:
        for key, value in a.items():
            if key == i["Area"]:
                value.append(("botton", minValue))


for x in calcData:
    for key, value in x.items():
        resi = ((float(value[0][1]) -
                 float(value[1][1]))/float(value[0][1]))*100
        value.append(("percent", resi))

statePercent = 12.43
for x in calcData:
    for key, value in x.items():
        if(key == "Statewide"):
            statePercent = value[2][1]
        resIndex = float(value[2][1])/statePercent
        value.append(("resIndex", resIndex))

exportData = {}
for x in calcData:
    for key, value in x.items():
        exportData[key] = value[3][1]


print(exportData)
with open('dataResIndexManu.json', 'w') as outfile:
    json.dump(exportData,  outfile, indent=4)
# calcData[i["Area"]]["bottom"] = minValue

# .update({"bottom": minValue})

# print(calcData)
# print(extractData["year"])
# if (i["data"]["year"] == "2020" and i["data"]["periodName"] == "March"):
#     print(i["data"]["value"])
