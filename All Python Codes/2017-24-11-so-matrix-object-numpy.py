
# coding: utf-8

# ## Matrix Object in Numpy
# Numpy, short for Numerical Python, is the fundamental package required for hight performance scientific computing and its best library to learn and apply on data science career.
# 
# This is just little illustration.
# 
# <img style="float: left;" src="https://www.safaribooksonline.com/library/view/python-for-data/9781449323592/httpatomoreillycomsourceoreillyimages1346880.png" width=400 height=200>

# In[1]:


import numpy as np


# In[2]:


a = np.array([[1,2,4],
              [2,5,3], 
              [7,8,9]])
A = np.mat(a)
A


# In[3]:


A = np.mat('1,2,4;2,5,3;7,8,9')
A


# In[5]:


a = np.array([[ 1, 2],
              [ 3, 4]])
b = np.array([[10,20], 
              [30,40]])

np.bmat('a,b;b,a')


# In[10]:


x = np.array([[4], [2], [3]])
x


# In[11]:


A * x


# In[12]:


print(A * A.I)


# In[13]:


print(A ** 3)

