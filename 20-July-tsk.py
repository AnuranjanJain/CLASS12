import pandas as p
d={'Item_Name':['Notebook','Pen','Inkpen','Notebook','Pen'],'Amount':[100,50,30,100,50],'Quantity':[2,5,3,3,5]}
df=p.DataFrame(d)
print(df)
print(df.pivot_table(df,index=['Amount','Quantity'],aggfunc='sum'))
