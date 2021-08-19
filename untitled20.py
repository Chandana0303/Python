import pymysql
try:
    d = pymysql.connect(host='localhost',
                    user='root',
                    password = 'Cloud@123$',
                    db='fis')

    cur = d.cursor()
    sql = "drop table test"
    cur.execute(sql)
    #print('record saved')
    #print("record deleted")
    print("table dropped")
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