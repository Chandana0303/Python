'''class employee:
    empno=0
    salary=0
    grade = ''
    def get(self,a,b):
        self.empno=a
        self.salary=b
    def check(self):
        if self.salary>30000:
            self.grade='A'
        else:
            self.grade='B'
    def show(self):
        self.check()
        print(self.empno)
        print(self.grade)
    
obj = employee()
#obj.empno=101
#obj.empname='ram'
obj.get(101,30000)
obj.show()  
'''
'''
class employee():
    empno = 101
    empname = 'ram'
    grade = 'A'
obj = employee()
print(hasattr(obj, 'empno'))
print(getattr(obj,'empname'))
setattr(obj,'empno',102)
print(getattr(obj,'empno'))
#delattr(obj,'empname')
#print(getattr(obj,'empname'))'''

#constructors
'''
class employee:
    empno=0
    salary=0
    grade=''
    #parameterised constructor
    def __init__(self,a,b,c):
        self.empno=a
        self.salary=b
        self.grade=c
        print("const.. called")
    def show(self):
        print(self.empno)
        print(self.salary)
        print(self.grade)
    def __del__(self):
        print("Byee..")
        
obj = employee(101,10000,'A')
#__init__ calls
obj.show()   
obj1 = employee(102,11000,'A')
#__init__ calls
obj1.show() 
    '''
#single level inheritance
class A:
    def hello(self):
        print("hello")
        print("function")
class B(A):
    def sum(self,a,b):
        print("sum is..",(a+b))    
obj = B()
obj.sum(5,4)
obj.hello()        

#multilevel inheritance
class A:
    def hello(self):
        print("hello")
        print("function")
class B(A):
    def sum(self,a,b):
        print("sum is..",(a+b)) 
class C(B):
    def Hi(self): 
        print("hi c..")
obj = C()
obj.Hi()
obj.sum(5,4)
obj.hello()

#multiple inheritance
class A:
    def hello(self):
        print("hello")
        print("function")
class B:
    def sum(self,a,b):
        print("sum is..",(a+b)) 
class C(A,B):
    def Hi(self): 
        print("hi c..")
obj = C()
obj.hello()
obj.sum(5,4)
obj.Hi()

#__str__ func
class A:
    def hello(self):
        print("hello")
        print("function")
    def __str__(self):
        return "MY class"
    
obj = A()
print(obj)

class A:
    def hello(self):
        __name ="raj"
obj = A()
print(obj.hello())        
            
