#type casting from int() to str()
x = 89
y = 9
#print(str(x)+str(y))

z=x+y
del z
#print('sum is:',z)

'''
a = [32,54.6,'abc',True,89,False]
print(a)
print(a[5])
print(a[3:5])
print(len(a))
#update
a[0] = 900
print(a)
#delete
del a[1]
print(a)

#nested list
b=[[32,54,89],['abc','def'],[True,False]]
print(b)

c=[1,7,4,3,10]
print(max(c))
print(min(c))
print(len(c))
'''

x = ['ab','be','cs','fb']
#print(x.insert(3, 'd'))
#print(x.append('i'))
#print(x)
#print(x.count('ab'))

r=['x','y','z','s']
#append of lists
#print(x.extend(r))
#print(x)
#print(x.index('be'))
#print(r.pop()) #removes last element
r.sort() #sorting of the list
r.reverse() #reverses the list
#print(r)

'''
s=[1,8,5,9,10,15,12]
t= sorted(s,reverse=True)
print(s)
print(t)
'''
#dictionary
empdata = {'empno':[101,102,103],'empname':['ram','ravi','arun'],'empsalary':[10000,20000,15000]}
#print(empdata['empname'])
#empdata['empsalary']=20000
'''print(empdata)
#del empdate['empname']
print(empdata['empsalary'])
print(empdata.keys())
print(empdata.values())
print(empdata.get('grade','N/A'))'''

a = {'grade':'A','leaves':40}
empdata.update(a) # a gets appended to s
#print(empdata)

a=empdata.copy()
#print(empdata)

b = {'name','city','age'}
c= dict.fromkeys(b)
#print(c)
#c.clear

e=dict.fromkeys(b,10)
e.clear()
print(e)

#Tuple
z = (10,4,'abc',True)
#z[1] =100 error
#del z[1] error

#set
f = {32,54,51,54,90}
print(len(f))
f.add(68)
print(f)
f.remove(90)
print(f)
