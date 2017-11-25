
# coding: utf-8

# ## Elementwise Operations and Statistics.
# In this section I will cover on Elementwise operations, Basic reductions, Broadcasting, and Sorting data. Arrays are important because they enable you to express batch operations on data without writing any for loops. This is usually called vectorization. Any arithmetic operations between equal-size arrays applies the operation elementwise:
# ### Here are the main steps we will go through
# * Element-wise operations
#     * Elementwise operations
#     * Basic reductions
#     * Broadcasting
#     * Sorting data
# * Do some statistics on numpy
# 
# This is just little illustration.
# <img src="https://s3.amazonaws.com/dq-content/6/numpy_ndimensional.svg">

# #### Basic operations

# In[1]:


import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9]])


# In[2]:


#elementwise add arr2 to arr1
np.add(arr1, arr2)


# In[3]:


#elementwise subtract arr2 from arr1
np.subtract(arr1, arr2)


# In[4]:


#elementwise multiply arr1 by arr2
np.multiply(arr1,arr2)


# In[5]:


#elementwise divide arr1 by arr2
np.divide(arr1, arr2)


# In[6]:


#elementwise raise arr1 raised to the power of arr2
np.power(arr1,arr2)


# In[7]:


#returns True if the arrays have the same elements and shape
np.array_equal(arr1,arr2)


# In[9]:


#square root of each element in the array
np.sqrt(arr1)


# In[26]:


#Transcendental functions:
#sine of each element in the array
np.sin(arr1)


# In[11]:


#natural log of each element in the array
np.log(arr1)


# In[12]:


#absolute value of each element in the array
np.abs(arr1)


# In[24]:


arr = np.random.random(9)
print("original array:\n ", arr)
#rounds up to the nearest int
np.ceil(arr)


# In[22]:


#rounds down to the nearest int
np.floor(arr)


# In[23]:


#rounds to the nearest int
np.round(arr)


# In[25]:


#Logical operations:
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
np.logical_or(a, b)


# #### Basic reductions

# In[27]:


x = np.array([1, 2, 3, 4])
np.sum(x)


# In[28]:


#Sum by rows and by columns:
x = np.array([[1, 1], [2, 2]])
x


# In[29]:


x.sum(axis=0)   # columns (first dimension)


# In[30]:


x[:, 0].sum(), x[:, 1].sum()


# In[31]:


x.sum(axis=1)   # rows (second dimension)


# #### Basic reductions
#  * Basic operations on numpy arrays (addition, etc.) are elementwise
# 
#  * This works on arrays of the same size.
#   Nevertheless, It’s also possible to do operations on arrays of different
#     sizes if NumPy can transform these arrays so that they all have
#     the same size: this conversion is called broadcasting.
#     The image below gives an example of broadcasting:

# In[32]:


a = np.tile(np.arange(0, 40, 10), (3, 1)).T
a


# In[33]:


b = np.array([0, 1, 2])
b


# In[34]:


a + b


# In[36]:


#We have already used broadcasting without knowing it!:
a = np.ones((4, 5))
a[0] = 2 
a


# #### Sorting data

# In[37]:


a = np.array([[4, 3, 5], [1, 2, 1]])
b = np.sort(a, axis=1)
b


# In[38]:


#Sorts each row separately!
a.sort(axis=1)
a


# In[45]:


s = np.array([[2,4,5,8,2,0,3,7]])
t = np.sort(s, axis=1)
t


# #### Do some statistics on numpy

# In[49]:


stat = np.arange(25).reshape(5,5)
stat


# In[50]:


#returns mean along specific axis
np.mean(stat, axis=0)


# In[51]:


#returns sum of arr
stat.sum()


# In[52]:


#returns minimum value of arr
stat.min()


# In[53]:


#returns maximum value of specific axis
stat.max(axis=0)


# In[54]:


#returns the variance of array
np.var(stat)


# In[55]:


#returns the standard deviation of specific axis
np.std(stat, axis=1)


# In[57]:


#returns correlation coefficient of array
np.corrcoef(stat)

