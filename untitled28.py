import matplotlib.pyplot as plt
'''
x=[10,20,30]
y=[20,10,15]

plt.plot(x,y,'--r')

x1 = [15,23,31]
y1 = [12,24,30]
plt.plot(x1,y1,'--g')'''

'''states = ['Bangalore','Mumbai','pune']
pop = [1.2,3.4,3.9] 
plt.plot(states,pop) 
plt.title("Pop in crore")
plt.xlabel("States")
plt.ylabel("Population")
plt.show()'''

sem1 = [1,3,5]
m1 = [34,90,65]
sem2 = [2,4,6]
m2= [54,76,43]

plt.bar(sem1,m1,color='r')
plt.bar(sem2,m2,color='b')
#plt.plot(sem,m1,label='Raj')
#plt.plot(sem,m2,label='amit')
plt.title("Bar plot")
#plt.xlabel('sem')
#plt.ylabel('marks')
plt.show()