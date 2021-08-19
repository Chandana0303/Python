import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
employee = {'empno':['e001','e002','e003'],
            'name':['ram','raj','vivek'],
            'salary':[12000,11000,13000]}
df = pd.DataFrame(employee)
df['tax'] = (30/100)*df['salary']
print(df)
plt.bar(df['name'],df['tax'])
plt.xlabel('name')
plt.ylabel('tax')
plt.show()'''

#horizontal barplot
'''country = ['India','US','UK']
pop = [1.8,2.1,1.5]
y = np.arange(len(country))
plt.barh(y,pop)
plt.xticks(y,country)
plt.title('pop chart')
plt.show()'''

#scatter plot
'''
x=[2,4,6,8]
y=[32,65,76,90]

plt.scatter(x,y)
plt.show()'''

#histogram
ages=[32,15,17,24,56,38,28]
plt.hist(ages,bins=5)
plt.show()

#piechart plot
labels = 'UP','MP','Delhi','Pune'
lit = [25,35,65,45]
col = ['green','blue','red','yellow']
e=(0,0,0,0.1)
plt.pie(lit,explode=e,labels=labels)
plt.show()

