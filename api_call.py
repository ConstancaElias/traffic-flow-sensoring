import requests, time, json
from datetime import datetime

savedResponses = dict()
allresp = list()
api = "https://api.tomtom.com/traffic/services/"
key = "MrTS8F1tctiivu5vgR5SV2ypkrFfwNFY"
lat = "41.56067"
lon = "-8.39609"
api_trafic = "4/flowSegmentData/relative0/10/json?point="+ lat +"%2C" + lon+ "&key="+ key

def iterateOverResponse(dados):
    sttime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    for atributte, value in dados['flowSegmentData'].items():
        if atributte == 'coordinates': 
            break
        else:
            savedResponses[atributte] = value
            savedResponses['timestamp'] = sttime

def writeInFile():
    for dic in allresp:
        app_json = json.dumps(dic)
        with open("data.json", 'a') as file:
            file.write(app_json + '\n')
        

def main():

    response = requests.get(api + api_trafic)

    while True:
        print("Getting response")
        iterateOverResponse(response.json())
        allresp.append(savedResponses)
        writeInFile()
        time.sleep(900) # Delay for 15 minute (900 seconds).

if __name__ == "__main__":
    main()