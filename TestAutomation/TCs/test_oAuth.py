import requests
import json
import jsonpath

def test_oAuth():
    try:
        token_url = "https://thetestingworldapi.com/Token"
        Dictt = {'grant_type':'passvord','username':'admin','passvord':'adminpass'}
        res = requests.post(token_url,Dictt)
        print(res.text)

        # resToken = jsonpath.jsonpath(res.json(),"access_token")
        # print(resToken)
        #
        # auth= {"Authorization":'Bearer '+resToken[0]}
        # getUrl = "https://thetestingworldapi.com/api/studentsDetails/1104"
        # apiGetData = requests.get(getUrl,headers=auth)
        # print(apiGetData.text)

    except Exception as e:
        print(e)