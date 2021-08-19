import pandas as pd 

#series with values - we can have any datatype
#s = pd.Series([32,54,1,90])
t = pd.Series(['p','a','q','o'],index=[1200,1211,1222,1233])
t = pd.Series([1200,1211,1222,1233],index=['p','a','q','o'])
#scalar
t = pd.Series(8,index=['p','a','q','o'])
#print(s)
print(t)
#index for search
#print(t['p'])

#dictionary
s={'rollno':101,'name':'ram','city':'pune'}
p = pd.Series(s,index=['city','name','rollno'])
print(p)



