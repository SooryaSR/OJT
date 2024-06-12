import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[1,2,3,4,5]
#plot
plt.plot(x,y1,label='y1',linestyle='-',color='g',linewidth=3,marker='o',markersize=8,markerfacecolor="violet")
plt.plot(x,y2,label='y2',linestyle='-.',color='r',linewidth=3,marker='x',markersize=8,markerfacecolor="yellow")
plt.title("customized line plot with grid")
plt.xlabel("x-axis")
plt.ylabel("y-label")
plt.legend()#legend method 
plt.grid(True)#add value a sgrid
plt.grid(color='aqua',linestyle='--',linewidth=1)#Customize grid
plt.show()
