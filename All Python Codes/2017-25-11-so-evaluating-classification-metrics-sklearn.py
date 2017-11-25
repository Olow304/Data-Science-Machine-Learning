
# coding: utf-8

# ## Evaluating Classification Metrics
# First, we'll try to build a model without cross-validation apply to it. Second, we'll use the same model with applying cross-validation and see if the accuracy score changed or not.
# 
# ### Main contents:
# ### Training and testing on the same data
#   * Rewards overly complex models that "overfit" the training data and won't necessarily generalize
# #### Train/test split
#   * Split the dataset into two pieces, so that the model can be trained and tested on different data
#   * Better estimate of out-of-sample performance, but still a "high variance" estimate
# #### K-fold cross-validation
#   * Systematically create "K" train/test splits and average the results together
#   * Even better estimate of out-of-sample performance
#   * Runs "K" times slower than train/test split
#   
# ### Model evaluation metrics
# ##### Classification problems: Classification accuracy
#   * There are many more metrics, here we'll cover on classification metrics
# 
# <img style="float:left;" src="https://image.slidesharecdn.com/finalcustlingprofiling-160226163538/95/customer-linguistic-profiling-10-638.jpg?cb=1456504658" width=600 height=300>

# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


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


# In[5]:


# set our X and y to data and target values
X , y = data_holder.data, data_holder.target


# In[6]:


# let's split into 70/30: train=70% and test=30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= .4, random_state = 0)


# In[7]:


print("X train shape: ", X_train.shape)
print("X test shape: ", X_test.shape)
print()
print("y train shape: ", y_train.shape)
print("y test shape: ", y_test.shape)


# In[8]:


# we'll set it to some parameters, but we'll go through depth on parameter tuning later
model = SVC(kernel='linear', C=1)
# fit our training data
model.fit(X_train, y_train)
#let's predict 
pred = model.predict(X_test)


# ### Accuracy Score
# Calling the accuracy_score class we can get the score of our model

# In[10]:


#accuracy score
from sklearn.metrics import accuracy_score
accuracy_score(y_test, pred)


# In[11]:


# let's get our classification report


# ### Classification Metrics
# Build a text report showing the main classification metrics

# In[12]:


#classification report
from sklearn.metrics import classification_report
print(classification_report(y_test, pred))


# ### Confusion Matrix
# A confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier") on a set of test data for which the true values are known.

# In[13]:


#confusion matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, pred))

