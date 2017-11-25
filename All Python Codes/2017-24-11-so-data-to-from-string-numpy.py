
# coding: utf-8

# ## Data to from String in Numpy
# Numpy, short for Numerical Python, is the fundamental package required for hight performance scientific computing and its best library to learn and apply on data science career.
# 
# This is just little illustration.
# 
# <img style="float: left;" src="http://community.datacamp.com.s3.amazonaws.com/community/production/ckeditor_assets/pictures/332/content_arrays-axes.png" width=600 height=400>

# In[1]:


import numpy as np


# In[2]:


a = np.array([[1,2],
           [3,4]], 
          dtype = np.uint8)


# In[3]:


a.tostring()


# In[5]:


a.tostring(order='F')


# In[8]:


s = a.tostring()
a = np.fromstring(s, dtype=np.uint8)
a


# In[9]:


a.shape = 2,2
a

