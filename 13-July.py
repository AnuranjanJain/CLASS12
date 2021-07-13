#Sorting
#1- .sort_values()--
#syntax= DataFrame.sort_values(ny=None,axis=0,ascending=True,inplace=False)
#asc=true and inplace=false = by default
import pandas as p
d={'Name':p.Series(['p1','p2','p3','p4','p5']),'Age':p.Series([26,27,25,24,31]),'Score':[87,89,67,55,47]}
df=p.DataFrame(d)
print(df)
df=df.sort_values(by='Score')
print("After Sort")
print(df)
print("After Sort , asc=False")
print(df.sort_values('Score',ascending=0))

#for multiple score
print("After Sort multiple columns")
print(df.sort_values(by=['Age','Score'],ascending=[True,False]))

#chamging index
df=df.reindex([1,4,3,2,0])
print(df)
#sort df by index in asc order
print(df.sort_index(ascending=False))

#changing the order of rows and columns in df and changing the order of data in series


#rename --

df1=df.rename(index={0:'1P',1:'2P',2:'3P'})
print(df1)
