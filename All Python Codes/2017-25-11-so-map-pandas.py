
# coding: utf-8

# ## Map function 
# Map values of Series using input correspondence (which can be a dict, Series, or function)
# 
# 

# In[55]:


import pandas as pd
import numpy as np


# In[56]:


data = pd.read_csv('data/train.csv')


# In[57]:


data.head()


# In[58]:


# let's convert 1 and 0 from sex column
data["Sex_Num"] = data.Sex.map({'female':0,'male':1})


# In[59]:


data.head()


# In[60]:


data.loc[0:4, ["Sex", "Sex_Num"]]


# In[61]:


# let's get the mean fare price using map function
data["mean_fare"] = data.Fare.map(lambda x: np.mean(x)a)


# In[62]:


data.loc[0:3, ["Fare","mean_fare"]]


# In[63]:


data["Embarked"].unique()


# In[64]:


data["Dummy_Embarked"] = data.Embarked.map({'S':0,'C':1,'Q':3,None:4})


# In[65]:


data.loc[0:4, ['Embarked','Dummy_Embarked']]

