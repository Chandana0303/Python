import pymysql
try:
    d = pymysql.connect(host='localhost',
                    user='root',
                    password = 'Cloud@123$',
                    db='fis')

    cur = d.cursor()
    #sql = "select version()"
    a = int(input("enter empno.."))
    b = input("enter name..")
    c= input("enter city..")
    e = int(input("enter salary.."))
    sql = "insert into employee values(%d,'%s','%s',%d)"%(a,b,c,e)
    #sql = "delete from employee where empno=102"
    #sql = "update employee set salary = 17000 where empno=104"
    cur.execute(sql)
    print('record saved')
    #print("record deleted")
    #print("record updated")
    d.commit()
    #data = cur.fetchall()
    '''for res in data:
    print('empno..',res[0])
    print('name..',res[1])
    print('city..',res[2])
    print('salary..',res[3])
    '''
except Exception as ex:
    print("error")    
d.close()