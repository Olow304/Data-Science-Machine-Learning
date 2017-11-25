
# coding: utf-8

# ## Preprocessing StandardScaler 

# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


from sklearn.datasets import load_iris
holder = load_iris()
X, y = holder.data, holder.target


# In[4]:


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state =0)


# ### StandardScaler 

# In[5]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)

