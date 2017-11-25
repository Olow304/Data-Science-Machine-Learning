
# coding: utf-8

# ## Evaluating Regression Metrics
# 
# ### Main contents:
# * Mean Absolute Error
# * Mean Squared Error
# * Rsquare Score
# 
# 

# ### Mean Absolute Error

# In[2]:


from sklearn.metrics import mean_absolute_error
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
mean_absolute_error(y_true, y_pred)


# In[3]:


y_true = [[0.5, 1], [-1, 1], [7, -6]]
y_pred = [[0, 2], [-1, 2], [8, -5]]
mean_absolute_error(y_true, y_pred)


# In[5]:


mean_absolute_error(y_true, y_pred, multioutput='raw_values')
mean_absolute_error(y_true, y_pred, multioutput=[0.3, 0.7])


# ### Mean Squared Error

# In[7]:


from sklearn.metrics import mean_squared_error
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
mean_squared_error(y_true, y_pred)


# In[8]:


y_true = [[0.5, 1],[-1, 1],[7, -6]]
y_pred = [[0, 2],[-1, 2],[8, -5]]
mean_squared_error(y_true, y_pred) 


# In[9]:


mean_squared_error(y_true, y_pred, multioutput='raw_values')

mean_squared_error(y_true, y_pred, multioutput=[0.3, 0.7])


# ### R-square Score
# R^2 (coefficient of determination) regression score function.
# Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of y, disregarding the input features, would get a R^2 score of 0.0.

# In[12]:


from sklearn.metrics import r2_score
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
r2_score(y_true, y_pred) 


# In[13]:


y_true = [[0.5, 1], [-1, 1], [7, -6]]
y_pred = [[0, 2], [-1, 2], [8, -5]]
r2_score(y_true, y_pred, multioutput='variance_weighted')


# In[14]:


y_true = [1,2,3]
y_pred = [1,2,3]
r2_score(y_true, y_pred)


# In[15]:


y_true = [1,2,3]
y_pred = [2,2,2]
r2_score(y_true, y_pred)


# In[16]:


y_true = [1,2,3]
y_pred = [3,2,1]
r2_score(y_true, y_pred)

