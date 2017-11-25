
# coding: utf-8

# ## Working with image plotting
# Introduction:
# 
# Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shell, the jupyter notebook, web application servers, and four graphical user interface toolkits.
# 
# ### Here are the main steps we will go through
# * How to add text to graph?
# 
# This is Just a little illustration.
# 
# <img style="float:left;" src="https://i.imgur.com/bFsdlJy.png"></img>

# In[23]:


import warnings
warnings.filterwarnings('ignore')


# In[24]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
get_ipython().magic('matplotlib inline')


# In[26]:


img = mpimg.imread('Beauty-Black-White-Wallpaper.jpg')


# In[27]:


img.shape


# In[28]:


imgplot = plt.imshow(img)


# In[29]:


lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)


# In[30]:


imgplot = plt.imshow(lum_img)
imgplot.set_cmap('hot')


# In[31]:


imgplot = plt.imshow(lum_img)
imgplot.set_cmap('spectral')


# In[32]:


imgplot = plt.imshow(lum_img)
imgplot.set_cmap('spectral')
plt.colorbar()
plt.show()


# In[33]:


imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0,0.7)

