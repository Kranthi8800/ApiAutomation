import requests

from requests.auth import HTTPBasicAuth

def test_BasicAuth():

    res=requests.get("https://github.com/login",auth=HTTPBasicAuth('kranthi8800@gmail.com','Kranthi@8861'))
    print(res.text)
