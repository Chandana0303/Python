#dataframe is a 2d structure
import pandas as pd
'''
a = {'rollno':[101,102,103,104],'name':['ram','raj','vivek','amit'],'marks':[91,86,94,87]}
d=[['amit',21],['vivek',32],['raj',29]]
df = pd.DataFrame(a,index=['rank2','rank4','rank1','rank3'])
print(df)
print(df['rollno'])
df['promote'] = df['marks']+10
print(df)'''

employee = {'empno':['e001','e002','e003'],
            'name':['ram','raj','vivek'],
            'basic':[12000,11000,13000]}
df = pd.DataFrame(employee,index=[1,2,3])
df['hra'] = (12/100)*df['basic']
print(df)
df['total']=df['hra']+df['basic']
print(df)
