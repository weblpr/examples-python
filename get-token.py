import requests
r = requests.get('http://api.weblpr.com/getDemoToken')
if r.status_code == 201:
  print "Token: " + r.text
else:
  print "Request failed: " + r.text