import urllib.parse
import requests
from datetime import datetime, date, timedelta
import csv

base_url = 'https://api.openweathermap.org/data/2.5/forecast?'

with open('city_id.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    city_id= []
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
    url = base_url + urllib.parse.urlencode({'id':city_id[i]}) + '&units=metric&appid=edd2edf8ee00f8c62066e3dbcd0e2497'
    print(url)
    data = requests.get(url).json()
    cnt = data['cnt'] - 1
    ime = repr(data['city']['name'])

    for j in range(cnt):
        temp = (data['list'][j]['main']['temp'])
        clouds = (data['list'][j]['clouds']['all'])
        opis = repr(data['list'][j]['weather'][0]['main'])
        desc = repr(data['list'][j]['weather'][0]['description'])
        txt = repr(data['list'][j]['dt_txt'])
        ura = int(txt[12:14])
        if( ura > 5 and ura < 21):
            templist.append(ime)
            templist.append(txt)
            templist.append(temp)
            templist.append(clouds)
            templist.append(opis)
            templist.append(desc)
        else:
            continue
        napoved.append(templist)
        templist = []

print(napoved)
with open("vreme_napoved.csv", "w", newline='') as f:
    writerCsv = csv.writer(f)
    writerCsv.writerows(napoved)
f.close()