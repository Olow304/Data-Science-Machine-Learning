import matplotlib.pyplot as plt 

#saves plot/figure to image
plt.savefig('pic_name.png')
#saves transparent plot/figure to image
plt.savefig('transparentback.png')

#customization:
#colors plot to color blue
plt.plot(x,y, color='lightblue')
plt.plot(x,y, alpha=0.4)
#mappable: the image, contourset etc to which colorbar applies
plt.colorbar(mappable, orientation='horizontal')
