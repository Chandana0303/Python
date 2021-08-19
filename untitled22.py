import pymysql

d = pymysql.connect(host='localhost',
                    user='root',
                    password = 'Cloud@123$',
                    db='fis')
try:
    a = int(input("enter empno.."))
    cur = d.cursor()
    sql = "select * from employee where empno=%d"%(a)
    cur.execute(sql)
    d.commit()
    data = cur.fetchone()
    if data != None:
        print("error")
    else:
        
        b = input("enter name..")
        c= input("enter city..")
        e = int(input("enter salary.."))
        sql = "insert into employee values(%d,'%s','%s',%d)"%(a,b,c,e)
        cur.execute(sql)
        print("record saved")
        d.commit()
    
except Exception as ex:
    print("error")    
d.close()