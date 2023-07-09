import requests
import json
import jsonpath

url="https://reqres.in/api/users?page=2"

#Fetch data

res = requests.get(url)

'''get status code'''
print(res)
''''get body data'''
# print(res.content)

'''Fetch specific content from the response & validate by converting json format'''
jp=json.loads(res.text)
# print(jp)

'''Fetch data using jason short path'''
pages = jsonpath.jsonpath(jp,'total')
assert pages[0]==12
print(pages[0])

'''Fetch data using jason Long path'''
pages = jsonpath.jsonpath(jp,'data[0].first_name')


'''Fetch data using jason Long path with looping'''

for i in range (0,3):

    pages = jsonpath.jsonpath(jp,'data['+str(i)+'].first_name')

    print(pages[0])