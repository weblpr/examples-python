import requests, json, base64

with open("n_bs47040.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

url = 'http://api.weblpr.com/requests'
payload = {'token': '59a6662f-e923-490c-a4b5-5d54d7e5d0ff', 'bytes': encoded_string}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
#print "Full response: ", r.text
response = r.json()
print "Request id: ", response["id"]
print "Plates found: ", len(response["plates"])
for k in response["plates"]:
  print k["number"]
 