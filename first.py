import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2]=="+":
        print(a+b)
    if sys.argv[2]=="-":
        print(a-b)
    if sys.argv[2]=="/":
        print(a/b)      
except ZeroDivisionError:
    print("check no.2")
except ValueError:
    print("check values entered") 
except IndexError:
    print("check index value")    




#print('hello world welcome')
#print(len(sys.argv))
#print(sys.argv[1])
#print('bye',sys.argv[0])

#uncaught exception
'''a = int(input("enter a no.."))
b = int(input("enter a no.."))
c = a/b
print("div..",c)'''


#try and except
try:
    a = int(input("enter a no.."))
    b = int(input("enter a no.."))
    c = a/b
    print("div..",c)
    
except Exception as ex:
    print("Any issue..",ex)

#try and except
try:
    a = int(input("enter a no.."))
    if(a<10):
        raise Exception()
    else:    
        print("ok")
    
except:
    print("Any issue..") 
   
finally:
    print("the ends..")    
