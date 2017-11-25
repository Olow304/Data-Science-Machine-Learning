
# coding: utf-8

# ## Cross Validation
# First, we'll try to build a model without cross-validation apply to it. Second, we'll use the same model with applying cross-validation and see if the accuracy score changed or not.
# 
# ### Main contents:
# * Build Support-Vector-Machine without cross-validation
# * Apply the same model with cross-validation
# 
# Note! We'll cover the metrics scores later
# 
# <img style="float:left;" src="https://cdn-images-1.medium.com/max/1600/1*J2B_bcbd1-s1kpWOu_FZrg.png" width=700 height=300>

# In[1]:


# libraries we need
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC


# In[4]:


# load iris dataset
data_holder = load_iris()
print(data_holder.data.shape)
print(data_holder.target.shape)


# In[6]:


# set our X and y to data and target values
X , y = data_holder.data, data_holder.target


# In[13]:


# split our data into train and test sets
# let's split into 70/30: train=70% and test=30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= .4, random_state = 0)


# In[22]:


print("X train shape: ", X_train.shape)
print("X test shape: ", X_test.shape)
print()
print("y train shape: ", y_train.shape)
print("y test shape: ", y_test.shape)


# In[16]:


# let's fit into our model, svc
# we'll set it to some parameters, but we'll go through depth on parameter tuning later
model = SVC(kernel='linear', C=1)
# fit our training data
model.fit(X_train, y_train)
# print how our model is doing
print("Score: ", model.score(X_test, y_test))


# As you can see our model scores 96% on our training data, we'll try to boost that accuracy score higher.
# 
# ### Computing cross-validated 
# The simplest way to use cross-validation is to call the cross_val_score helper function on the estimator and the dataset.

# In[20]:


# call cross-validation library
from sklearn.model_selection import cross_val_score
model = SVC(kernel='linear', C=1)

# let's try it using cv
scores = cross_val_score(model, X, y, cv=5)


# #### Evaluate Model
# Here is the output of our 5 KFold cross validation. Each value is the accuracy score of the support vector classifier when leaving out a different fold. There are three values because there are three folds. A higher accuracy score, the better.

# In[19]:


scores


# To get an good measure of the model's accuracy, we calculate the mean of the three scores. This is our measure of model accuracy.

# In[18]:


# print mean score
print("Accuracy using CV: ", scores.mean())


# ## I'll be updating more on this section!
