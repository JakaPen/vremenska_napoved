import urllib.parse
import requests
from datetime import datetime, date, timedelta
import csv

base_url = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/'

with open('city_id_dan.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    city_id = []
    mesto = []
    for row in readCSV:
        id = row[0]
        mesto1 = (row[1])

        city_id.append(id)
        mesto.append(mesto1)

print(city_id)
print(mesto)

templist = []
napoved = []


for i in range(len(city_id)):
    url = base_url + city_id[i] + '?apikey=EEKik13eqaXpUWxv7DtAd98D5BiJvAJJ&metric=true'
    data = requests.get(url).json()
    ime = mesto[i]
    print(url)
    for j in range(5):
        datum = (data['DailyForecasts'][j]["Date"][:10])
        tempmin = (data['DailyForecasts'][j]['Temperature']['Minimum']['Value'])
        tempmax = (data['DailyForecasts'][j]['Temperature']['Maximum']['Value'])
        vremeikona = (data['DailyForecasts'][j]['Day']['Icon'])
        vremeopis = (data['DailyForecasts'][j]['Day']['IconPhrase'])
        templist.append(ime)
        templist.append(datum)
        templist.append(tempmin)
        templist.append(tempmax)
        templist.append(vremeikona)
        templist.append(vremeopis)
        napoved.append(templist)
        templist = []

print(napoved)
with open("vreme_napoved_dan.csv", "w", newline='') as f:
    writerCsv = csv.writer(f)
    writerCsv.writerows(napoved)
f.close()


