import pymysql
import numpy as np
import matplotlib.pyplot as plt

d = pymysql.connect(host='localhost',
                    user='root',
                    password = 'Cloud@123$',
                    db='fis')
cur = d.cursor()
sql = "select empname,salary from employee"
    #sql = "insert into employee values(106,'jhon','mumbai',18000)"
    #sql = "delete from employee where empno=102"
    #sql = "update employee set salary = 17000 where empno=104"
cur.execute(sql)
    #print('record saved')
    #print("record deleted")
    #print("record updated")
    #d.commit()
data = cur.fetchall()
empname = []
salary = []
for res in data:
    empname.append[res[0]]
    salary.append(res[3])
print('empname..',res[0])
print('salary..',res[3])
        
plt.bar(empname,salary)
plt.legend()
plt.xlabel('Name')
plt.ylabel('salary')
plt.show()

d.close()
      
