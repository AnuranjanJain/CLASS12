#types of style of charts
#solid
#dashed
#dashed doted
#doted
import pandas as p
import matplotlib.pyplot as m
d={'X':[1,2,3,4,5],'Y':[2,6,4,8,3]}
df=p.DataFrame(d)
m.plot(df['X'],df['Y'],'r',linestyle='--',marker='v',markeredgecolor='r',label='Temp')  #markeredgecolor used to change color of marker edge
#check ss for further details


#to plot label
m.xlabel('Week')
m.ylabel('Temp')

#to display title
m.title('Temp per Week')

#to display label
m.legend(loc='upper right')  #left / right  lower / upper

m.show()
