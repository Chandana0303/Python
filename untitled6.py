#no value pass no return
'''
def Hello():
    print("hi")
    print("hello")

print("first")
Hello()
print("second")
Hello()

#value pass and no return
def calc(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
calc(90,4)    

#value pass 2nd way of doing it
def calc(a,b): #a & b are formal parameters
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
#x & y are actual parameters
x = int(input("enter a number"))
y = int(input("enter a number"))
calc(x,y)

#return
def fact(x):
    f=1
    while x>=1:
        f=f*x
        x = x-1
    return f

r = int(input("number"))
d = fact(r)
print("fact is..",d)
    '''

#making a list to dictionary
'''def employee(t):
    d = {}
    d['empno'] = t
    return d
    
a = [101,102,103,104]
s = employee(a)
print(s)'''

'''
def show(no,name,city):
    print("No..",no)
    print("Name..",name)
    print("city..",city)
    
show(101,'ram','pune')   
show(city="mumbai",no=102,name="ram")
'''

#Function with default parameters
'''
def details(name="test",age=0,salary=0):
    print("Name..",name)
    print("Age..",age)
    print("Salary..",salary)
    
details("ram",25,10000)
details()
details("shyam",5000)    
'''

#function with variable arguments
'''
def showdata(*x):
    for m in x:
        print("values",m)

showdata(10)
showdata(10,20,30)
showdata(10,20,30,40)
showdata('abc',40,'xyz',60)  
'''

#sum 
def sum1(*x):
    sum1 = 0
    for i in x:
        sum1 = sum1+i
    return sum1

print(sum1(1,2,4,5))

#call by reference
def change(d):
    d.append(1000)
    
r = [24,56,73,64]
change(r)
print(r)

#global variable 
def Hi():
    global a
    print(a)
    a='hello'
    print(a)
    
a = "my python"
Hi()    

#lambda function
a = lambda x,y:x+y
print(a(3,5))

#generator function
def basicgen():
    yield 'a'
    yield 'b'
    yield 'c'
 
x = basicgen()    
print(next(x))
print(next(x))
print(next(x))    

def basicgen1(x):
    for a in range(x):
        yield a
 
x = basicgen1(10)    
print(next(x))
print(next(x))
print(next(x))

x = [1,2,3,4]
y = [var for var in x if var%2==0]
print(y)