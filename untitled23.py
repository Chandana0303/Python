import numpy as np
#1-D array
#x = np.array([12,13,15])
#2-D array
#y = np.array([[1,2,3],
            #[4,5,6],
             #[7,8,9],
             #[10,11,12]])'''

#print(y.shape) gives size of array
#y.shape = (2,6) shapes the array to 2x6 matrix
#z =y.reshape(6,2) reshapes the array
#print(z)

#1-D array
'''x = np.arange(3,30)
print(x)'''

#by step size
'''x = np.arange(5,51,5)
y = x.reshape(5,2)
print(y)'''

#1-D array of 0 values
#x = np.zeros(5)
#x = np.zeros((3,3)) #2-D array of zero values
#x = np.ones(5) #1-d array of one values
#x = np.ones((3,3)) #2-d array of one values
x = np.linspace(10,50,7) #10-50  even spaced,7 values
print(x)