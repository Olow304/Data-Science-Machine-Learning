
# coding: utf-8

# ## Grid Search
# 
# Hyper-parameters are parameters that are not directly learnt within estimators. In scikit-learn they are passed as arguments to the constructor of the estimator classes. Typical examples include C, kernel and gamma for Support Vector Classifier, alpha for Lasso, etc.

# In[2]:


# Load libraries
import numpy as np
from sklearn.datasets import load_iris
from sklearn import linear_model
from sklearn.model_selection import GridSearchCV


# In[3]:


# Load data
iris = load_iris()
X = iris.data
y = iris.target


# ### create logistic regression

# In[4]:


logistic = linear_model.LogisticRegression()


# ### Create regularization penalty space

# In[5]:


penalty = ['l1', 'l2']

# Create regularization hyperparameter space
C = np.logspace(0, 4, 10)

# Create hyperparameter options
hyperparameters = dict(C=C, penalty=penalty)


# ### Create grid search using 10-fold cross validation

# In[6]:


clf = GridSearchCV(logistic, hyperparameters, cv=10)


# ### Fit grid search

# In[15]:


best_model = clf.fit(X, y)


# In[9]:


# View best hyperparameters
print('Best Penalty:', best_model.best_estimator_.get_params()['penalty'])
print('Best C:', best_model.best_estimator_.get_params()['C'])


# ### Predict target vector

# In[10]:


best_model.predict(X)


# In[14]:


best_model.score(X,y)

