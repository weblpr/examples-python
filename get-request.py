import sys, requests, json

id = sys.argv[1]

token = '59a6662f-e923-490c-a4b5-5d54d7e5d0ff'
r = requests.get('http://api.weblpr.com/requests/' + id + '?token=' + token)
response = r.json()
print "Numbers found: ", [ plate["number"] for plate in response["plates"] ]