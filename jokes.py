import requests as req

url = "https://sv443.net/jokeapi/v2/joke/Any"

res = req.get(url)

rec_data = res.json()

for data in rec_data.keys():
    if data !='flags' and data !='id' and data !='lang':
        print("{}: {}".format(data,rec_data[data]))
