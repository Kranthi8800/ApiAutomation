import requests
import json
import jsonpath


url = "https://reqres.in/api/users"
try:
    jsonFile = open("D:\TestAutomation\GeneralFiles\jsn.json",'r')
    jsonfiledata = jsonFile.read()

    print(jsonfiledata)

    jsondata = json.loads(jsonfiledata)

    print(jsondata)

    res = requests.post(url,jsondata)

    print(res.content)



    assert res.status_code==201

    print(res.headers)
    print(res.headers.get("Content-Length"))

    # ress = requests.get(res)
    ress = json.loads(res.text)

    fetchData= jsonpath.jsonpath(ress,"id")
    print(fetchData[0])

except Exception as e:
    print(e)