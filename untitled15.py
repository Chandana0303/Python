class MyException(Exception):
    def showmessage(self):
        print("My issue..")
try:
    a=int(input("enter a number"))
    if a<10:
       raise MyException()
    else:
        print("ok")
        
except MyException as ex:
    ex.showmessage()
    
    
#asserterror
a = int(input('number..'))  
assert a<10  
    