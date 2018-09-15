import requests 
r = requests.get('http://ip.jsontest.com')
print("Response object:", r)
print("Response text:", r.text)