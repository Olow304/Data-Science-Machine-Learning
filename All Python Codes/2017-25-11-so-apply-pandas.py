
# coding: utf-8

# ## Apply function 
# Subset rows or columns of dataframe according to labels in the specified index.
# 
# Note that this routine does not filter a dataframe on its contents. The filter is applied to the labels of the index.

# In[105]:


import pandas as pd
import numpy as np


# In[106]:


data = pd.read_csv('data/train.csv')


# In[107]:


data.head(4)


# In[108]:


# let's use apply function to get the length of names
data["Name_length"] = data.Name.apply(len)


# In[109]:


data.loc[0:5, ["Name", "Name_length"]]


# In[110]:


# let's get the mean price on fare column
data["Fare_mean"] = data.Fare.apply(np.mean)


# In[111]:


data.loc[0:5, ["Fare", "Fare_mean"]]


# In[112]:


data.Name.str.split('.')[0][0].split(',')[1]


# In[113]:


# let's get the name perfix, like Mr. Mrs. Mss. Ms...
data['prefix'] = data.Name.str.split('.').apply(lambda x: x[0].split(',')[1])


# In[114]:


data.loc[0:10, ['Name', 'prefix']]


# In[115]:


del data['dummy_prefix']


# In[117]:


data.tail()


# In[116]:


# let's get the unique prefix
data['prefix'].unique()


# In[118]:


# let's use apply function to combined prefixes, 
# male = Mr Master, Don, rev, Dr, sir, col, capt, == 0
# female = Mrs miss, Mme, Ms, Lady, Mlle, the countess,Jonkheer  == 1


# In[119]:


dummy_pre = data.groupby('prefix')


# In[120]:


#list(data.groupby('prefix'))


# In[121]:


dummy_pre.count()


# In[122]:


get_dummy = data.prefix


# In[126]:


pd.get_dummies(data['prefix'])


# In[125]:


data.head()

