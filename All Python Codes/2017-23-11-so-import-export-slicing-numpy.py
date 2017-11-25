
# coding: utf-8

# ## Importing, Exporting, Basic Slicing and Indexing.
# In terms of the importing and exporting files I would not go depth on it. You can refer the docstring for complete information on the various ways it can be used. A few examples will be given here in regard to this. I would spent sometime on the slicing and indexing arrays.
# ### Here are the main steps we will go through
# * How to use loadtxt, genfromtxt, and savetxt?
# * How to slice and index array?
# 
# This is just little illustration.
# <img src="http://www.bogotobogo.com/python/images/python_strings/string_diagram.png">

# #### How to use loadtxt, genfromtxt, and savetxt??
# * <b>numpy.loadtxt()</b> : Load data from a text file. This function aims to be a fast reader for simply formatted files. 
# * <b>numpy.genfromtxt()</b>: Load data from a text file, with missing values handled as specified. When spaces are used as delimiters, or when no delimiter has been given as input, there should not be any missing data between two fields. When the variables are named (either by a flexible dtype or with names, there must not be any header in the file (else a ValueError exception is raised). Individual values are not stripped of spaces by default. When using a custom converter, make sure the function does remove spaces.
# * <b>numpy.savetxt()</b>: Save an array to a text file. Further explanation of the fmt parameter (%[flag]width[.precision]specifier):
# 
# ##### Example 
# Here is the general idea, I'll come back to it.

# In[2]:


import numpy as np 
# using numpy you can load text file
np.loadtxt('file_name.txt')
# load csv file
np.genfromtxt('file_name.csv', delimiter=',')
# you can write to a text file and save it
np.savetxt('file_name.txt', arr, delimiter=' ')
# you can write to a csv file and save it
np.savetxt('file_name.csv', arr, delimiter=',')


# #### How to slice and index array?
# <b>ndarrays</b> can be indexed using the standard Python x[obj] syntax, where x is the array and obj the selection. There are three kinds of indexing available: field access, basic slicing, advanced indexing. Which one occurs depends on obj.
# 
# The basic slice syntax is i:j:k where i is the starting index, j is the stopping index, and k is the step (k\neq0). This selects the m elements (in the corresponding dimension) with index values i, i + k, ..., i + (m - 1) k where m = q + (r\neq0) and q and r are the quotient and remainder obtained by dividing j - i by k: j - i = q k + r, so that i + (m - 1) k < j.
# 
# Check the docstring for complete information on the various ways it can be used. A few examples will be given here:

# In[9]:


# slicing 1 to 7 gives us: [1 through 6]
slice_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
slice_array[1:7]


# In[12]:


# if we do this, we are giving k, which is the step function. in this case step by 2
slice_array[1:7:2]


# In[21]:


slice_arrays = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])+1
#return the element at index 5
slice_arrays[5]


# In[25]:


#returns the 2D array element on index value of 2 and 5
slice_arrays[[2,5]]


# In[30]:


#assign array element on index 1 the value 4
slice_arrays[1] = 100
#assign array element on index [1][3] the value 10
slice_arrays[[1,3]] = 100
slice_arrays


# In[64]:


#return the elements at indices 0,1,2 on a 2D array:
slice_arrays[0:3]


# In[65]:


#returns the elements at indices 1,100
slice_arrays[:2]


# In[66]:


slice_2d = np.arange(16).reshape(4,4)
slice_2d


# In[67]:


#returns the elements on rows 0,1,2, at column 4
slice_2d[0:3, :4]


# In[72]:


#returns the elements at index 1 on all columns
slice_2d[:, 1]


# In[84]:


# return the last two rows
slice_2d[-2:10]
# returns the last three rows
slice_2d[1:]


# In[85]:


# reverse all the array backword
slice_2d[::-1]


# In[86]:


#returns an array with boolean values
slice_2d < 5


# In[87]:


#inverts a boolearn array, if its positive arr - convert to negative, vice versa
~slice_2d


# In[91]:


#returns array elements smaller than 5
slice_2d[slice_2d < 5]

