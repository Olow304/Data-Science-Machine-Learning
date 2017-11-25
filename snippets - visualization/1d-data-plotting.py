import matplotlib.pyplot as plt 

#plot data connected by lines
lines = plt.plot(x,y)
#creats a scatterplot, unconnected data points
plt.scatter(x,y)
#simple vertical bar chart
plt.bar(xvalue, data, width, color...)
#simple horizontal bar
plt.barh(yvalues, data, width, color...)
#plots a histogram
plt.hist(x,y)
#box and whisker plot
plt.boxplot(x,y)
#creates violin plot
plt.violinplot(x,y)
#fill area under/between plots
ax.fill(x,y, color='lightblue')
ax.fill_between(x,y, color='yellow')