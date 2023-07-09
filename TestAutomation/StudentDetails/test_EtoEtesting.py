import requests
import jsonpath
import json
import pytest

def test_AddUser():

    url = "https://thetestingworldapi.com/api/studentsDetails"
    fileData = open("D:/TestAutomation/GeneralFiles/RequestsJson.json",'r')
    fRead = fileData.read()
    jData = json.loads(fRead)
    res = requests.post(url,jData)
    print(res.text)
    id = jsonpath.jsonpath(res.json(),'id')
    print(id[0])

    #add technical skill
    url2 = "https://thetestingworldapi.com/api/technicalskills"
    fileData1 = open("D:/TestAutomation/GeneralFiles/technicalSkill.json", 'r')
    jData1 = json.loads(fileData1.read())
    jData1["id"]=int(id[0])
    jData1["st_id"]=id[0]
    ress = requests.post(url2,jData1)

    print(ress.text)

    #add Address skill
    url3 = "https://thetestingworldapi.com/api/addresses"
    fileData2 = open("D:/TestAutomation/GeneralFiles/Address.json", 'r')
    jData2 = json.loads(fileData2.read())

    jData2["st_id"] = id[0]
    resss = requests.post(url3, jData2)
    print(resss.text)

    #get complete details (here we are used Request chaining , id of POST request used in Get  request to fetch data)

    url4 = f"https://thetestingworldapi.com/api/FinalStudentDetails/{id[0]}"

    ressss = requests.get(url4)
    jD = ressss.json()
    print(jD)

    jspd = jsonpath.jsonpath(jD,"data")
    print(jspd)






