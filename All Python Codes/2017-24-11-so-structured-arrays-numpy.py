
# coding: utf-8

# ## Structured Arrays in Numpy
# Numpy, short for Numerical Python, is the fundamental package required for hight performance scientific computing and its best library to learn and apply on data science career.
# 
# This is just little illustration.
# 
# <img style="float: left;" src="http://slideplayer.com/6419067/22/images/5/NumPy+Array.jpg" width=600 height=400>

# In[1]:


import numpy as np


# In[3]:


a = np.array([1.0,2.0,3.0,4.0], np.float32)


# In[22]:


# called the function view on our data
a.view(np.complex64)


# In[21]:


# assign our to data to dtype
my_dtype = np.dtype([('mass', 'float32'), ('vol', 'float32')])


# In[8]:


a.view(my_dtype)


# In[9]:


my_data = np.array([(1,1), (1,2), (2,1), (1,3)], my_dtype)
print(my_data)


# In[10]:


my_data[0]


# In[11]:


my_data[0]['vol']


# In[12]:


my_data['mass']


# In[13]:


my_data.sort(order=('vol', 'mass'))
print(my_data)


# In[14]:


person_dtype = np.dtype([('name', 'S10'), ('age', 'int'), ('weight', 'float')])


# In[15]:


person_dtype.itemsize


# In[16]:


people = np.empty((3,4), person_dtype)


# In[17]:


people['age'] = [[33, 25, 47, 54],
                 [29, 61, 32, 27],
                 [19, 33, 18, 54]]


# In[18]:


people['weight'] = [[135., 105., 255., 140.],
                    [154., 202., 137., 187.],
                    [188., 135., 88., 145.]]


# In[19]:


print(people)


# In[20]:


people[-1,-1]

