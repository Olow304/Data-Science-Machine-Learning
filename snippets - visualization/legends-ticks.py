import matplotlib.pyplot as plt 

#Legends:
#sets title of plot
plt.title('Just goes here')
#sets label next to x-axis
plt.xlabel('x-axis')
#sets label next to y-axis
plt.ylabel('y-axis')
#set title and axis labels
ax.set(title='axis', ylabel='y-axis', xlabel='x-axis')
#no overlapping plot elements
ax.legend(loc='best')

#Ticks:
#set ticks
plt.xticks(x, labels, rotation='vertical')
#set x-ticks
ax.xaxis.set(ticks=range(1,5), ticklabels=[3,100,-12,"foo"])
#make y-ticks longer and it go in and out
ax.tick_params(axis='y', direction='inout', length=10)
