#It will overwrite
# obj = open("D:\TXT.txt", 'w')

#Append the data

obj = open("D:\TXT.txt", 'a+')
obj.write("Written data into a file")
obj.close()
obj = open("D:\TXT.txt", 'r')
print(obj.readline())
print(obj.tell())
obj.seek(2)
print(obj.tell())
print(obj.readline())
print(obj.tell())