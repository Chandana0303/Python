import numpy as np 

x = np.array([[32,1,6],
              [9,15,20],
              [30,7,5],
              [13,24,18]])
z = np.array([[1,2,3],
            [4,5,7],
             [6,8,9],
             [10,11,12]])
#slicing start 2,gap 2, till 6
#y = slice(2,7,2) method 1
#y = x[2:7:2] #method 2
#print(z[...,2]) #any row 2 column
#print(z[2,...]) #any 2 row value
#print(z[...,1:])#any row col 1 onwards

#conditional data
#print(z[z>5])
'''
print(x+z)
print(x-z)
print(x/z)
print(x*z)'''

'''print(z.T) #Transpose
print(np.transpose(z))
print(np.mod(x,z))
print(np.add(x,z))
print(np.subtract(x,z))
print(np.multiply(x,z))
print(np.divide(x,z))'''

'''
print(x.flatten())#converts 2d to 1d array
print(x.flatten(order='F'))#transposes column wise
print(np.concatenate((x,z))) #concatenates
print(np.concatenate((x,z),axis=1))#concatenates row wise
'''

#z = np.split(x,2)
#print(np.unique(z))
'''
print(np.amin(x))#min
print(np.amin(x,0))#min clo wise
print(np.amin(x,1))#min row wise
print(np.amax(x))#max
print(np.amax(x,0))#max col wise
print(np.amax(x,1))#max row wise
'''

print(np.mean(x))
print(np.median(x))