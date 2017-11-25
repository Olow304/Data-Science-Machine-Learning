
# coding: utf-8

# ## LabelEncoder
# Encode labels with value between 0 and n_classes-1.
# 

# In[1]:


import warnings
warnings.filterwarnings('ignore')


# In[6]:


from sklearn import preprocessing
# call our labelEncoder class
le = preprocessing.LabelEncoder()
# fit our data
le.fit([1, 2, 2, 6])
# print classes
le.classes_
# transform
le.transform([1, 1, 2, 6]) 
#print inverse data
le.inverse_transform([0, 0, 1, 2])


# In[9]:


le = preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])

list(le.classes_)

le.transform(["tokyo", "tokyo", "paris"]) 

#list(le.inverse_transform([2, 2, 1]))

