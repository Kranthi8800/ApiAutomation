import requests

url="https://reqres.in/api/users?page=2"

#Fetch data

res = requests.get(url)

'''get status code'''
print(res)
''''get body data'''
# print(res.content)

''''Header of the res'''
print(res.headers)

'''Validate status code'''
# print(res.status_code)
# assert res.status_code==200

'''Fetch specific header content'''

print(res.headers.get("Date"))
print(res.headers.get("Server"))

'''Fetch Cookies coming in the header'''
print(res.cookies)

'''Fetch Encoding'''
print(res.encoding)

'''Fetch Elapse time (Request&Response time duration)'''
print(res.elapsed)
