#var fn 
import pandas as p
d={'Age':p.Series([87,89,67,55])}
df=p.DataFrame(d)
print(df['Age'].var())
