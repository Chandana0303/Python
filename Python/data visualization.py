import pandas as pd

'''
data = {'unemployment':[2.3,3.4,1.2,0.8,8.7,9.5],
        'market-share':[1200,1100,1300,1500,800,900]}

df = pd.DataFrame(data,columns=['unemployment',
                                'market-share'])

print(df)
df.plot(x='unemployment',y='market-share',
        kind='scatter')'''

'''
data = {'year':[1980,1999,2002,2005,2017],
        'pop':[50,72,81,98,111]}

df = pd.DataFrame(data,columns=['year',
                                'pop'])
df.plot(x='year',y='pop',kind='line')#line->default
'''

data = {'country':['India','US','UK'],'gdp':[5,7,9]}

df = pd.DataFrame(data,columns=['country','gdp'])
                                
df.plot(x='country',y='gdp',kind='bar')
 
    