import requests
import json

headers = {'Content-type': 'application/json'}

informationIDsManufacturing = ['LASST450000000000005', "LAUMT131226000000005",
                               "LAUMT451670000000005", "LAUMT371674000000005", "LAUMT451790000000005",
                               "LAUMT452486000000005", "LAUMT454390000000005", "LAUMT454494000000005"]

data = json.dumps(
    {"seriesid": informationIDsManufacturing, "startyear": "2018", "endyear": "2021"})
p = requests.post(
    'https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)

json_data = json.loads(p.text)
print(json_data)
json_data = json_data['Results']["series"]

extraInfo = {}

extraInfo['LASST450000000000005'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "true",
    "Area":	"Statewide",
    "Industry":	"General"
}
extraInfo['LAUMT131226000000005'] = {
    "State":	"Georgia",
    "Seasonaly Adjusted": "false",
    "Area":	"Augusta-Richmond County, GA-SC",
    "Industry":	"General"
}
extraInfo['LAUMT451670000000005'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Charleston-North Charleston, SC",

    "Industry":	"General"
}
extraInfo['LAUMT371674000000005'] = {
    "State":	"North Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Charlotte-Concord-Gastonia, NC-SC",
    "Supersector": "Manufacturing",
    "Industry":	"General"
}
extraInfo['LAUMT451790000000005'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Columbia, SC",
    "Industry":	"General"
}
extraInfo['LAUMT452486000000005'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Greenville-Anderson-Mauldin, SC",

    "Industry":	"General"
}

extraInfo['LAUMT454390000000005'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Spartanburg, SC",

    "Industry":	"General"
}
extraInfo['LAUMT454494000000005'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Sumter, SC",

    "Industry":	"General"
}
for x in informationIDsManufacturing:
    for s in range(len(json_data)):
        if json_data[s]["seriesID"] == x:
            json_data[s]['State'] = extraInfo[x]["State"]
            json_data[s]['Area'] = extraInfo[x]["Area"]
            json_data[s]['Industry'] = extraInfo[x]["Industry"]
        for item in json_data[s]['data']:
            item["date"] = item["periodName"] + ", " + item['year']


with open('dataGeneral.json', 'w') as outfile:
    json.dump(json_data,  outfile, indent=4)
