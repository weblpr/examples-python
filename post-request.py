#!/usr/bin/python
import sys, getopt
from os import listdir
from os.path import isfile, join
import requests, json, base64

def main(argv):
    token = ''
    path = ''
    usage = 'Usage: post-request.py -t <token> -p <path>'
    try:
      opts, args = getopt.getopt(argv,"ht:p:",["token=","path="])
    except getopt.GetoptError:
      print "Invalid argument(s). ", usage
      sys.exit(2)
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print usage
         sys.exit()
      elif opt in ("-t", "--token"):
         token = arg
      elif opt in ("-p", "--path"):
         path = arg
    
    url = 'http://api.weblpr.com/requests'
    headers = {'content-type': 'application/json'}
    waitForDone = True

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

if __name__ == "__main__":
   main(sys.argv[1:])
