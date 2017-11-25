import matplotlib.pyplot as plt 

#Text:
#places text at coordinates 1/1
plt.text(1,1, 'Example text', style='italic')
#annotate the point with coordinates xy with text 
ax.annotate('some annotation', xy=(10,10))
#just put math formula
plt.title(r'$delta_i=20$',fontsize=10)

#Limits:
#sets x-axis to display 0 - 7
plt.xlim(0,7)
#sets y-axis to display -0.5 - -9
plt.ylim(-0.5,-9)
#sets limits
ax.set(xlim=[0,7], ylim[-0.5,-9])
ax.set_xlim(0,7)
#set margins: add padding to a plot, values 0 - 1
plt.margins(x=1.0, y=1.0)
#set the aspect ratio of the plot to 1
plt.axis('equal')