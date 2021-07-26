import matplotlib.pyplot as m
w=[1,2,3,4,5,6,7,8]
t=[28,34,36,30,32,38,34,32]
tt=[30,32,34,28,30,35,33,30]
# check ss for table
# marker= -- to mark
# markersize= -- to inc size of marker
m.plot(w,t,'r',linestyle='--',marker='h',markersize='20')
m.plot(w,tt,'g',linestyle='-.',marker='o')
m.show()
