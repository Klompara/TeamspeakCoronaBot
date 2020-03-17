# !/usr/bin/python
# coding=utf-8

import time
import ts3
import json
import requests
from datetime import datetime

if __name__ == "__main__":
    from def_param import *
    while True:
        try:
            response = requests.get('https://corona.lmao.ninja/countries')
            countryArray = json.loads(response.text)
            infectedAmount = 0
            infectedAmountNew = 0
            deadAmount = 0
            deadAmountNew = 0
            recovered = 0
            critical = 0
            for country in countryArray:
                if country["country"] == "Austria":
                    #print(country)
                    infectedAmount = country["cases"]
                    infectedAmountNew = country["todayCases"]
                    deadAmount = country["deaths"]
                    deadAmountNew = country["todayDeaths"]
                    recovered = country["recovered"]
                    critical = country["critical"]
            try:
                with ts3.query.TS3Connection(HOST, PORT) as ts3conn:
                    ts3conn.login(client_login_name=USER, client_login_password=PASS)
                    ts3conn.use(sid=SID)
                    respInf = ts3conn.channelfind(pattern="Infizierte")
                    respTote = ts3conn.channelfind(pattern="Tote")
                    respRecovered = ts3conn.channelfind(pattern="Geheilte")

                    now = datetime.now()
                    date_time = "Letzte aktualisierung am: " + now.strftime("%m/%d/%Y, %H:%M:%S")
                    try:
                        ts3conn.channeledit(cid=respInf.parsed[0]["cid"], channel_name="[cspacer]Infizierte: " + str(infectedAmount) + " (+" + str(infectedAmountNew) + ")", channel_description=date_time)
                    except ts3.query.TS3QueryError as ex:
                        print("Infected amount is same: " + str(ex))
                    try:
                        ts3conn.channeledit(cid=respTote.parsed[0]["cid"], channel_name="[cspacer]Tote: " + str(deadAmount) + " (+" + str(deadAmountNew) + ")", channel_description=date_time)
                    except ts3.query.TS3QueryError as ex:
                        print("Dead amount is same: " + str(ex))
                    try:
                        ts3conn.channeledit(cid=respRecovered.parsed[0]["cid"], channel_name="[cspacer]Geheilte: " + str(recovered) + " Kritisch: " + str(critical), channel_description=date_time)
                    except ts3.query.TS3QueryError as ex:
                        print("Cured/Critical is same: " + str(ex))
            except ts3.query.TS3QueryError as ex:
                print("Query error: " + str(ex))
            except Exception as ex:
                print("Something went wrong: " + str(ex))
        except Exception as ex:
            print("Error when fetching data from REST-API: " + str(ex))
        time.sleep(300)