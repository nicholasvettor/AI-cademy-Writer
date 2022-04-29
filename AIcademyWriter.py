import requests
import json
import datetime

#------------------------------------

claim = input("Claim: " + "")

name = input("Name: " + "")

#------------------------------------

r = requests.post("https://api.deepai.org/api/text-generator", data={'text':claim}, headers={'api-key': 'API KEY HERE'})

decode = json.loads(r.text)
output = decode['output']
output = output.encode("ascii", "ignore")
output = output.decode()

#-----------------------------

date = datetime.date

print(str(date.today()))

#-----------------------------

names = claim.replace(" ", "")

print(names)

#-----------------------------

jsonfile = json.dumps({'name':name, 'date':str(date.today()), 'contents':output}, separators=(',', ':'))

print(jsonfile)

#-----------------------------

fp = open(names + '.json', 'x')
fp.write(jsonfile)
fp.close()