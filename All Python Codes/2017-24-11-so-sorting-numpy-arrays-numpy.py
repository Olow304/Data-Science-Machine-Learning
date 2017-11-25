
# coding: utf-8

# ## Sorting arrays in Numpy
# Numpy, short for Numerical Python, is the fundamental package required for hight performance scientific computing and its best library to learn and apply on data science career.
# 
# 

# In[3]:


import numpy as np


# In[9]:


names = np.array(['F', 'C', 'A', 'G'])
weights = np.array([20.8, 93.2, 53.4, 61.8])

sort(weights)


# In[10]:


#argsort
ordered_indices = np.argsort(weights)
ordered_indices


# In[11]:


weights[ordered_indices]


# In[13]:


names[ordered_indices]


# In[15]:


data = np.array([20.8,  93.2,  53.4,  61.8])
data.argsort()


# In[16]:


# sort data
data.sort()
data


# In[17]:


# 2d array
a = np.array([
        [.2, .1, .5], 
        [.4, .8, .3],
        [.9, .6, .7]
    ])
a


# In[18]:


sort(a)


# In[20]:


# sort by column
sort(a, axis = 0)


# In[22]:


# search sort
sorted_array = linspace(0,1,5)
values = array([.1,.8,.3,.12,.5,.25])


# In[24]:


np.searchsorted(sorted_array, values)

