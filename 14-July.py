#deleting index -- to del index of df
#-- reset_index() -- used to del index in df
#-- drop()
#syntax         df.reset_index().drop(index)
#               or
#               df.drop(index=[])


#todays task

#sort in desending order

import pandas as p
d={'Name':p.Series(['Jeet','Dheeraj','Suraj','Rohit','Ankit']),'Age':p.Series([26,25,25,24,31]),'Score':[87,89,67,55,47]}
df=p.DataFrame(d)
print('Reindex')
df1=df.reindex([1,4,3,2,0])
print(df1)

print('Des order')
print(df.sort_index(ascending=False))


#variance -- check ss
#syntax   -- print(df[].var())
print(df['Age'].var())

#standard devuiation -- sd is measured as the spread of data distro in the given data set
#standard devuiation= mean(abs(x-x.mean()))
#syntax -- print(df[].std())
print(df['Age'].std())print(df[].std())
