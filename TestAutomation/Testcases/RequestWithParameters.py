import requests


parameters = {'t1':'k','t2':'g'}
url = "https://httpbin.org/get"

res = requests.get(url,params=parameters)

print(res.text)
print(res.elapsed)