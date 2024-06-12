import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[2,3,6,7,10,16]

plt.plot(x,y,marker='*',linestyle='-', color='g',markersize=6, markerfacecolor='r')
plt.title("Line plot with markers")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()