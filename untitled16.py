'''empno = input("enter empno.")
name = input("enter name.")
city = input("enter city.")

fn = input('filename')
#append
obj = open(fn,'a')

obj.write(str(empno)+'\n')
obj.write(str(name)+'\n')
obj.write(str(city)+'\n')

print("data saved")
obj.close()'''

#read

import datetime

d= datetime.datetime.now()
x = input('enter file to read')
fo = open(x,'r')
st = fo.read(2000)
if d.day==1:
    y = input('enter second file')
    fw = open(y,'a')
    fw.write(st)
print("done")

fo.close()
fw.close()
    

   
        

  
