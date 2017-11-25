
# coding: utf-8

# ## Preprocessing Binarization 

# In[3]:


import warnings
warnings.filterwarnings('ignore')


# In[4]:


from sklearn.datasets import load_iris
holder = load_iris()
X, y = holder.data, holder.target


# In[5]:


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state =0)


# ### Binarizer 

# In[6]:


from sklearn.preprocessing import Binarizer
binarizer = Binarizer(threshold=0.0).fit(X)
binary_X = binarizer.transform(X)


# In[13]:


X[0:4]


# In[12]:


binary_X[0:4]

