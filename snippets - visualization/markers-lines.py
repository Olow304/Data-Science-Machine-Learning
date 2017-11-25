import matplotlib.pyplot as plt 

#add * for every data point
plt.plot(x,y, marker='*')
#adds dot for every data point
plt.plot(x,y, marker='.')

#lines:
#sets line width
plt.plot(x,y, linewidth=2)
#sets linestyle, ls can be ommitted
plt.plot(x,y, ls='solid')
#sets linestyle, ls can be ommitted
plt.plot(x,y, ls='--')
#lines are '--' and '_',
plt.plot(x,y, '--', x**2, y**2, '-.')
#sets properties of plot lines
plt.setp(lines, color='red', linewidth=2)