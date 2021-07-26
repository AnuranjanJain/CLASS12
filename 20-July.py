#pivot_table-pivoting with aggregation --

#when u hv duplicate values for only one index or one column , then pivot_table() mthd is used
#this mthd is used to convert row into column and vice versa . it allow grouping of any data field

import pandas as p
name={'INVIGILATOR':['R1','A1','N1','R1'],'Amount':[500,510,520,530]}
df=p.DataFrame(name)
print(df)
print(df.pivot_table(df,index='INVIGILATOR',aggfunc='sum'))
print(df.pivot_table(df,index='INVIGILATOR',aggfunc='max'))
