
# coding: utf-8

# ## Loading Data in Sklearn
# You can load your data from different formats or you can use build on data from sklearn
# 

# In[7]:


# we can just create random data
import numpy as np 
X = np.random.random((11,5))
y = np.array(['M','M','F','F','M','F','M','M','F','F','F'])
X[X < 0.7] = 0


# In[8]:


#use model selection to split our data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


# In[10]:


X_train.shape


# In[14]:


X_test.shape


# In[12]:


y_train.shape


# In[13]:


y_test.shape


# ### using datasets from sklearn

# In[17]:


import sklearn.datasets as data


# In[22]:


get_ipython().magic('pinfo2 data')


# In[25]:


# print all datasets
data.__all__ 


# In[21]:


# we can get all of this data
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_boston
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_digits
from sklearn.datasets import load_files
from sklearn.datasets import load_iris
from sklearn.datasets import load_linnerud
from sklearn.datasets import load_sample_images
from sklearn.datasets import load_sample_image
from sklearn.datasets import load_wine


# In[33]:


lbc = load_breast_cancer()
print("load_breast_cancer", lbc.data.shape)
print("load_breast_cancer", lbc.target.shape)


# In[35]:


lb = load_boston()
print("load_boston: ", lb.data.shape)
print("load_boston: ", lb.target.shape)


# In[36]:


ld = load_digits()
print("load_digits: ", ld.data.shape)
print("load_digits: ", ld.target.shape)


# In[37]:


lr = load_iris()
print("load_iris: ", lr.data.shape)
print("load_iris: ", lr.target.shape)


# you can do more with it...
