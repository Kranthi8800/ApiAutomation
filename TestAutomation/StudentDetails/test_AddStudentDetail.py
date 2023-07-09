import requests
import json
import jsonpath
import pytest

@pytest.fixture()
def CommonExecution():
    print("This function is used to fetch common data's")
    global url,fileData,res
    url = "https://thetestingworldapi.com/api/studentsDetails"
    fileData = open("D:/TestAutomation/GeneralFiles/RequestsJson.json",'r')


def test_AddStudentDetail(CommonExecution):

    jsonData = json.loads(fileData.read())
    print(jsonData)
    res = requests.post(url, jsonData)
    print(res.text)
    jsonD = json.loads(res.text)
    id = jsonpath.jsonpath(jsonD, "id")
    print(id)



def test_readReasposedata(CommonExecution):

    try:

        jsonData = json.loads(fileData.read())
        res = requests.post(url, jsonData)

        jsonD = json.loads(res.text) # else use -> jsonD = res.json()



        id = jsonpath.jsonpath(jsonD,"id")

        '''get details'''

        # url2 = f"https://thetestingworldapi.com/api/studentsDetails/{id[0]}"
        url2 = f"https://thetestingworldapi.com/api/studentsDetails/7621611"


        print(url2)



        ress = requests.get(url2)

        jd = json.loads(ress.text)
        print(jd)
        jsd = jsonpath.jsonpath(jd,"data.id")
        print(jsd)
        print("----------------------------------------------------------")


        # '''update data '''

        url3 = f"https://thetestingworldapi.com/api/studentsDetails/7621611"
        print(url3)
        f1 = open("D:/TestAutomation/GeneralFiles/putUpdateJson.json",'r')
        jsonData1 = json.loads(f1.read())
        print(jsonData1)
        res = requests.put(url3, jsonData1)
        print(res.text)
        jsonD1 = json.loads(res.text)
        print(jsonD1)
        id1 = jsonpath.jsonpath(jsonD1, "id")
        print(id1)

        print("-------------------fullupdate is done---------------")

        # '''Partial update'''
        url4 = f"https://reqres.in/api/users/2"
        print(url4)
        f2 = open("D:/TestAutomation/GeneralFiles/patchUpdate.json",'r')

        jsonData2 = json.loads(f2.read())
        print(jsonData2)
        res = requests.patch(url4, jsonData2)
        print(res.text)
        jsonD2 = json.loads(res.text)
        print(jsonD2)
        id2 = jsonpath.jsonpath(jsonD2, "id")
        print(id2)

        # '''Delete Details'''

        url5 = f"https://thetestingworldapi.com/api/studentsDetails/7621611"
        print(url5)
        f1 = open("D:/TestAutomation/GeneralFiles/putUpdateJson.json", 'r')
        jsonData1 = json.loads(f1.read())
        print(jsonData1)
        res = requests.put(url5, jsonData1)
        print(res.text)
        print(res.status_code)
        jsonD1 = json.loads(res.text)
        print(jsonD1)
        id1 = jsonpath.jsonpath(jsonD1, "id")
        print(id1)
        assert id1[0]==7621611
    except Exception as e:
        print(e)


# def test_abc():
#     print("Hello")
#     print()
#     print(id1)




