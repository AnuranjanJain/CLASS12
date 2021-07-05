#CH2- Data Handling Using Pandas - II
#DataAggregation
#DataAggregation is the process of turning the values of dataset into 1 single value.
#EG = the most common methods to peform Aggregation are min ,max ,sum ,count.
import pandas as p
import numpy as n
d={'Name':['A','V','S','D','f','g'],'Age':[26,24,23,22,23,24],'Score':[85,63,55,77,31,77]}
df=p.DataFrame(d)
print(df)

#max()  is used to find maximum value from a given set of values or column of df or a series
#syntax - df['column_name'].max()
d1=df['Age'].max()
print(d1)
#min() is used to find minium  value from a given set of values or column of df or a series
#syntax - df['column_name'].min()
d2=df['Age'].min()
print(d2)
#sum()
dd=df['Age'].sum()
print(dd)
#df['column_name'].min(skipna=True) = by deault
#df['column_name'].min(skipna=False) display only NaN


#count() - used to get the no. of values present in the column (doesnot count NaN values)
d3=df['Age'].count()
print(d3)
#axis fn dd=df['Age'].sum(asix=1)
