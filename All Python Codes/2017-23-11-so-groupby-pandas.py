
# coding: utf-8

# ## Groupby
# <b>DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, **kwargs)</b>
# 
# Group series using mapper (dict or key function, apply given function to group, return result as series) or by a series of columns.
# 
# ### Any groupby operation involves one of the following operations on the original object. They are −
# 
# * Splitting the Object
# 
# * Applying a function
# 
# * Combining the results
# 
# <img style="float: left;" src="https://i.stack.imgur.com/sgCn1.jpg"></img>

# In[1]:


# import library
import pandas as pd


# In[4]:


data = {'Students': ['S1', 'S2', 'S3', 'S3', 'S1',
         'S4', 'S4', 'S3', 'S2', 'S2', 'S4', 'S3'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Grade':[87,79,83,73,74,81,56,78,94,70,80,69]}
df = pd.DataFrame(data)
df


# ### Split Data into Groups
# Pandas object can be split into any of their objects. There are multiple ways to split an object like −
# 
# * obj.groupby('key')
# * obj.groupby(['key1','key2'])
# * obj.groupby(key,axis=1)
# 
# Let us now see how the grouping objects can be applied to the DataFrame object

# In[7]:


# let's groupby students
df.groupby('Students')


# In[8]:


# to view groups 
df.groupby('Students').groups


# In[9]:


# you can group by with multiple columns 
df.groupby(['Students','Year']).groups


# In[11]:


# iterating through groups
grouped = df.groupby('Students')
for student, group_name in grouped:
    print(student)
    print(group_name)


# In[13]:


# select group by value
grouped = df.groupby('Year')
print(grouped.get_group(2014))


# In[16]:


# find the mean of grouped by data
import numpy as np
grouped = df.groupby('Year')
print(grouped['Grade'].agg(np.mean))


# In[18]:


# find the average for all students
grouped = df.groupby('Students')
print(grouped['Grade'].agg(np.mean).round())


# In[19]:


# count 
grouped = df.groupby('Year')
print(grouped['Grade'].value_counts())


# In[21]:


#Filtration filters the data on a defined criteria and returns the subset of data. 
#The filter() function is used to filter the data.
# we are going to find the top 3 students
df.groupby('Students').filter(lambda x: len(x) >= 3)


# ### I'll be updating this notebook soon!
# using real dataset!!
