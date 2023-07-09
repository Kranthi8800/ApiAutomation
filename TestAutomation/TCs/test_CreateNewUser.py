import requests
import json
import jsonpath
import pytest

@pytest.fixture() #@pytest.fixture(scope="module") this method execute once in a while
def startExe():
    global url,jsonFile
    url = "https://reqres.in/api/users"
    jsonFile = open("D:\TestAutomation\GeneralFiles\jsn.json", 'r')
    yield
    print("_______________________________________________________________")
    print("Executed Successfully")

a=5
@pytest.mark.Sanity
#@pytest.Mark.*** are Decorators
@pytest.mark.skipif(a>10, reason="Condition is not satisfied")
def testCreateUser(startExe):
    try:

        jsonfiledata = jsonFile.read()

        print(jsonfiledata)

        jsondata = json.loads(jsonfiledata)

        print(jsondata)

        res = requests.post(url,jsondata)

        print(res.content)



        assert res.status_code==201

    except Exception as e:
        print(e)

@pytest.mark.Smoke
def testValidateCreateUser(startExe):
    try:
        jsonFile = open("D:\TestAutomation\GeneralFiles\jsn.json", 'r')
        jsonfiledata = jsonFile.read()

        print(jsonfiledata)

        jsondata = json.loads(jsonfiledata)

        print(jsondata)

        res = requests.post(url, jsondata)

        print(res.content)

        # assert res.status_code == 201

        print(res.headers)
        print(res.headers.get("Content-Length"))

        # ress = requests.get(res)
        ress = json.loads(res.text)

        fetchData = jsonpath.jsonpath(ress, "id")
        print(fetchData[0])

    except Exception as e:
        print(e)

'''use below command to execute perticular testcase in the directory
    python -m pytest -s -k testValidateCreateUser TCs
    Also execute partial test - python -m pytest -s -k test TCs :- "Here it execute both test case it has name test"
'''