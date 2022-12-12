#%%
import requests

url = 'https://api.transport.nsw.gov.au/v1/traffic/historicaldata'
headers = {
  'Accept': 'application/json', 
  'Content-Type': 'application/json', 
  'Apikey':  'uhcodPWssB4a0rKzFlogU9toEC7w0Z6XaRol'
}
body = {
  "showHistory": True,
  "created": "2020-06-01T00:00:00.000+10:00",
  "end": "2020-06-01T23:59:59.999+10:00",
  "radius": 1,
  "latitude": -33.86734,
  "longitude": 151.20823
}


r = requests.get(url, headers=headers)
print(r.text)
r.status_code
# %%
