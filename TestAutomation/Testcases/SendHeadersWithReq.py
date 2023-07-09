
import requests


hd = {'t1':'k','t2':'g'}
url = "https://httpbin.org/get"

res = requests.get(url,headers=hd)

print(res.text)

