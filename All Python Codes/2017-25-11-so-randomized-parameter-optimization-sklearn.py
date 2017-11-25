
# coding: utf-8

# ## Randomized Parameter Optimization
# 
# While using a grid of parameter settings is currently the most widely used method for parameter optimization, other search methods have more favourable properties. RandomizedSearchCV implements a randomized search over parameters, where each setting is sampled from a distribution over possible parameter values. This has two main benefits over an exhaustive search:

# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


# Load libraries
import numpy as np
from sklearn.datasets import load_iris
from sklearn import linear_model
from sklearn.grid_search import RandomizedSearchCV


# In[4]:


# Load data
iris = load_iris()
X = iris.data
y = iris.target


# In[11]:


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state =0)


# ### create logistic regression

# In[16]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()


# ### params build up

# In[17]:


params = {"n_neighbors" : range(1,5), "weights": ["uniform", "distance"]}


# In[18]:


rsearch = RandomizedSearchCV(estimator=knn, 
                             param_distributions=params, 
                             cv=4, n_iter=8,
                             random_state=5)


# In[19]:


rsearch.fit(X_train, y_train)


# In[20]:


print(rsearch.best_score_)


# In[21]:


print(rsearch.best_estimator_)

