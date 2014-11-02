import requests
r = requests.get('http://api.weblpr.com/getDemoToken')
print r.text