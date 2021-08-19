#position 
'''f = open('data1.txt','r')
#attributes of file 
print(f.closed)
print(f.mode)
print(f.name)

st = f.read(150)
print(st)
pos = f.tell()
print("position",pos)
pos = f.seek(0,0)
st = f.read(10)
print(st)
f.close()'''

import os
#print(os.getcwd())
#os.mkdir('newpython')
#print("new folder created")

#deleting folder
#os.rmdir('newpython')
#print("new folder removed")

#to rename a file
#os.rename('Data.txt','data3.txt')
#print("file renamed")

#to remove file
#os.remove('data3.txt')
#print("removed")

#to check if the file path exists or not
print(os.path.exists('data1.txt'))

print(os.name) #nt - incase of windows os

d = os.listdir('C:/Users/User/Desktop/Python')
print(d)
