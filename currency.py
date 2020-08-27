import requests

url = "https://currencyapi.net/api/v1/rates?key=aMYQlEHbLHzFOf0pPkTNG450T88XXa6Wfk1M"

response = requests.get(url)

recived_data = response.json()


for data in recived_data.keys():
    if data == 'rates':
        rates = recived_data[data]
        for rt in rates:
           # print("{}: {}".format(rt, rates[rt]))
           if rt == 'INR':
               rupee_rate = rates[rt]

dollars = int(input("enter your amount dollars: "))
inramt = dollars*rupee_rate
print(inramt)