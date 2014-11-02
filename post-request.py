import sys
from os import listdir
from os.path import isfile, join

import requests, json, base64

token = '59a6662f-e923-490c-a4b5-5d54d7e5d0ff' # please enter valid token
url = 'http://api.weblpr.com/requests'
headers = {'content-type': 'application/json'}
waitForDone = True

path = sys.argv[1]
files = [ join(path,f) for f in listdir(path) if isfile(join(path,f)) ]

for filename in files:
  with open(filename, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
  payload = {'token': token, 'bytes': encoded_string, 'waitForDone': waitForDone}
  print "Sending file: ", filename
  r = requests.post(url, data=json.dumps(payload), headers=headers)
  response = r.json()
  print "Request id: ", response["id"]
  if waitForDone:
    print "Numbers found: ", [ plate["number"] for plate in response["plates"] ]