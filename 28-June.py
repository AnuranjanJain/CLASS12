import pandas as p
d={'no':[1,2,3,4,5],'val1':['a','b','c','d','e'],'val2':['q','w','e','r','t']}
dd={'no':[2,3,6,7],'val1':['m','b','c','n'],'val2':['j','g','f','x']}
d1=p.DataFrame(d)
d2=p.DataFrame(dd)
d3=p.merge(d1,d2,on='no',how='inner')
print(d1)
print(d2)
print(d3)
print("RAW")
print(d)
