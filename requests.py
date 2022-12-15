import time
import requests
import json
from tinydb import TinyDB, Query

db = TinyDB('./base_dados.json')

while True:
    try:
        url_2 = "https://api.sportsanalytics.com.br/api/v1/fixtures-svc/fixtures/livescores"
        querystring_2 = {"include":"weatherReport,additionalInfo,league,stats,pressureStats,probabilities"}
        payload_2 = ""
        headers_2 = {
            "cookie": "route=f69973370a0dd0883a57c7b955dfc742; SRVGROUP=common",
            "authority": "api.sportsanalytics.com.br",
            "accept": "application/json, text/plain, */*",
            "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "origin": "https://playscores.com",
            "referer": "https://playscores.com/",
            "sec-ch-ua": "^\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\^Windows^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }

        response = requests.request("GET", url_2, data=payload_2, headers=headers_2, params=querystring_2)
        dic_response = response.json()        
        db.truncate()

        for game in dic_response['data']:
            dict_game = game
            db.insert(dict_game)        
    except:
        pass

    try:
        url_1 = "http://106.52.88.125/b365/soccer/test/oneHd2allEv/C1-G15"

        payload_1 = ""
        r = requests.request("GET", url_1, data=payload_1)
        dic_r = r.json()
        dados = dic_r

        for jogo in dados:
            dict_game = jogo
            db.insert(dict_game)            
    except:
        pass
    time.sleep(90)
