import requests, time, json
from datetime import datetime

allresp = list()
api = "https://api.tomtom.com/traffic/services/"
key = "MrTS8F1tctiivu5vgR5SV2ypkrFfwNFY"
lat = "41.551791086003234"
lon = "-8.421615692790999"
api_trafic = "4/flowSegmentData/relative0/10/json?point="+ lat +"%2C" + lon+ "&key="+ key

def iterateOverResponse(dados):
    sttime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    savedResponses = dict()
    for atributte, value in dados['flowSegmentData'].items():
        if atributte == 'coordinates':
            break
        else:            
            savedResponses['timestamp'] = sttime
            savedResponses[atributte] = value
    allresp.append(savedResponses)
    with open("data.json", 'a') as file:
        file.write(json.dumps(savedResponses) + '\n')

  
def main():
    #print(response.json())
    while True:
        print("Getting response")    
        response = requests.get(api + api_trafic)
        iterateOverResponse(response.json())
        time.sleep(30) # Delay for 15 minute (900 seconds).

if __name__ == "__main__":
    main()