
# coding: utf-8

# ## Preprocessing Normalization 

# In[4]:


import warnings
warnings.filterwarnings('ignore')


# In[5]:


from sklearn.datasets import load_iris
holder = load_iris()
X, y = holder.data, holder.target


# In[6]:


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state =0)


# ### Normalizer 

# In[7]:


from sklearn.preprocessing import Normalizer
scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)

