import requests
import json

headers = {'Content-type': 'application/json'}

informationIDsManufacturing = [
    'SMS45000003000000001', "SMU13122603000000001", "SMU45167003000000001", "SMU37167403000000001", "SMU45179003000000001", "SMU45248603000000001", "SMU45439003000000001", "SMU45449403000000001"]

data = json.dumps(
    {"seriesid": informationIDsManufacturing, "startyear": "2018", "endyear": "2021"})
p = requests.post(
    'https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)

json_data = json.loads(p.text)

json_data = json_data['Results']["series"]


extraInfo = {}

extraInfo['SMS45000003000000001'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "true",
    "Area":	"Statewide",
    "Supersector": "Manufacturing",
    "Industry":	"Manufacturing"
}
extraInfo['SMU13122603000000001'] = {
    "State":	"Georgia",
    "Seasonaly Adjusted": "false",
    "Area":	"Augusta-Richmond County, GA-SC",
    "Supersector": "Manufacturing",
    "Industry":	"Manufacturing"
}
extraInfo['SMU45167003000000001'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Charleston-North Charleston, SC",
    "Supersector": "Manufacturing",
    "Industry":	"Manufacturing"
}
extraInfo['SMU37167403000000001'] = {
    "State":	"North Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Charlotte-Concord-Gastonia, NC-SC",
    "Supersector": "Manufacturing",
    "Industry":	"Manufacturing"
}
extraInfo['SMU45179003000000001'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Columbia, SC",
    "Supersector": "Manufacturing",
    "Industry":	"Manufacturing"
}
extraInfo['SMU45248603000000001'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Greenville-Anderson-Mauldin, SC",
    "Supersector": "Manufacturing",
    "Industry":	"Manufacturing"
}

extraInfo['SMU45439003000000001'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Spartanburg, SC",
    "Supersector": "Manufacturing",
    "Industry":	"Manufacturing"
}
extraInfo['SMU45449403000000001'] = {
    "State":	"South Carolina",
    "Seasonaly Adjusted": "false",
    "Area":	"Sumter, SC",
    "Supersector": "Manufacturing",
    "Industry":	"Manufacturing"
}

for x in informationIDsManufacturing:
    for s in range(len(json_data)):
        if json_data[s]["seriesID"] == x:
            json_data[s]['State'] = extraInfo[x]["State"]
            json_data[s]['Area'] = extraInfo[x]["Area"]
            json_data[s]['Industry'] = extraInfo[x]["Industry"]
        for item in json_data[s]['data']:
            item["date"] = item["periodName"] + ", " + item['year']


with open('dataManufacturing.json', 'w') as outfile:
    json.dump(json_data,  outfile, indent=4)
