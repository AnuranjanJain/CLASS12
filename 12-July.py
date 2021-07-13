#groupby --a groupby fn involves one of the following operation on df
# 1- splitting the df
# 2- applying the fn
# 3- combining the result
import pandas as p
d={'Key':['A','B','C','A','B','C','B'],'data':[1,2,3,4,5,6,8]}
df=p.DataFrame(d)
print(df.groupby('Key').sum())
#can apply all previous fn of 5-july
import pandas as p
dd={'Date':['1-1-2019','1-1-2019','1-2-2019','1-2-2019','1-3-2019','1-3-2019'],'City':['delhi','delhi','Mumbai','Mumbai','Chennai','Chennai'],'Temp':[28,30,22,24,32,34]}
df=p.DataFrame(dd)
print(df.groupby('Temp').max())
