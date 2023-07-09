import requests
import json
import jsonpath


url = "https://reqres.in/api/users/2"
try:
    jsonFile = open("D:\TestAutomation\GeneralFiles\jsn.json",'r')
    jsonfiledata = jsonFile.read()

    print(jsonfiledata)

    jsondata = json.loads(jsonfiledata)

    print(jsondata)

    res = requests.put(url,jsondata)

    print(res.status_code)
    assert res.status_code==200
    print(res.content)

    jsd = json.loads(res.text)

    print()
    print(jsd)
    jsp = jsonpath.jsonpath(jsd,"job")

    print()
    print(jsp)




except Exception as e:
    print(e)