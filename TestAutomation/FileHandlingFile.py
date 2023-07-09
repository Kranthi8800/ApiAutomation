
#Opening File

obj = open("D:\TestAutomation\TXT.txt", 'r')

'''Read Full data from file'''
# print(obj.read())

'''Read lineByLine '''
# print(obj.readline())

'''Read few character from the file'''
# print(obj.read(3))

'''Read Character by Character'''

# for i in obj.read():
#     print(i)

'''Read data line by line from file'''

a= obj.readline()

while(a):
    print(a)
    a=obj.readline()