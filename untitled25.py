import numpy as np 

x = np.array([[0,1,2],
              [12,0,5],
              [3,6,0],
              [7,0,0]])
#print(np.nonzero(x))

#string handling
a = "this Is PYthOn"
print(np.char.lower(a))
print(np.char.upper(a))
print(np.char.title(a))
print(np.char.capitalize(a))
b = np.char.replace(a,'this','that')
print(b)
print(np.char.multiply('hello',5))
print(np.char.add('hello','Pyhton'))
