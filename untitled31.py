import pymysql
import numpy as np
import matplotlib.pyplot as plt

d = pymysql.connect(host='localhost',
                    user='root',
                    password = 'Cloud@123$',
                    db='fis')
cur = d.cursor()
sql = "select ename,salary from employee"
   
cur.execute(sql)
data = cur.fetchall()
ename = []
salary = []
for res in data:
    ename.append(res[0])
    salary.append(res[1])
        
plt.bar(ename,salary)
plt.xlabel('Name')
plt.ylabel('salary')
plt.show()

d.close()
      
