
# coding: utf-8

# ## Creating and Combining DataFrame
# <b>class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)</b>
# 
# Two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). Arithmetic operations align on both row and column labels. Can be thought of as a dict-like container for Series objects. 
# 
# <b>class pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)</b>
# One-dimensional ndarray with axis labels (including time series).
# 
# Labels need not be unique but must be a hashable type. The object supports both integer- and label-based indexing and provides a host of methods for performing operations involving the index. Statistical methods from ndarray have been overridden to automatically exclude missing data (currently represented as NaN).
# 
# ### Here are the main steps we will go through
# * How to create dataframe using pandas?
# * How to combine two data set using pandas?
# 
# This is Just a little illustration.
# 
# <img style="float: left;" src="https://www.tutorialspoint.com/python_pandas/images/structure_table.jpg"></img>

# In[5]:


import pandas as pd
import numpy as np


# #### How to create dataframe using pandas?

# In[16]:


# working with series
#create a series
s = pd.Series(np.random.randn(5))
#create a dataframe column
df = pd.DataFrame(s, columns=['Column_1'])
df 


# In[8]:


#sorting 
df.sort_values(by='Column_1')


# In[10]:


#boolean indexing
#It returns all rows in column_name,
#that are less than 10
df[df['Column_1'] <= 1]


# In[230]:


# creating simple series
obj2 = pd.Series(np.random.randn(5), index=['d', 'b', 'a', 'c', 'e'])
obj2


# In[20]:


obj2.index


# In[229]:


# returns the value in e
obj2['e']


# In[26]:


# returns all values that are greater than -2
obj2[obj2 > -2]


# In[27]:


# we can do multiplication on dataframe
obj2 * 2


# In[28]:


# we can do boolean expression
'b' in obj2


# In[228]:


# returns false, because 'g' is not defined in our data
'g' in obj2


# In[39]:


#Let's see we have this data
sdata = {'Cat': 24, 'Dog': 11, 'Fox': 18, 'Horse': 1000}
obj3 = pd.Series(sdata)
obj3


# In[227]:


# defined list, and assign series to it
sindex = ['Lion', 'Dog', 'Cat', 'Horse']
obj4 = pd.Series(sdata, index=sindex)
obj4


# In[226]:


# checking if our data contains null
obj4.isnull()


# In[44]:


#we can add two dataframe together
obj3 + obj4


# In[224]:


# we can create series calling Series function on pandas
programming = pd.Series([89,78,90,100,98])
programming


# In[223]:


# assign index to names
programming.index = ['C++', 'C', 'R', 'Python', 'Java']
programming


# In[102]:


# let's create simple data
data = {'Programming': ['C++', 'C', 'R', 'Python', 'Java'],
        'Year': [1998, 1972, 1993, 1980, 1991],
        'Popular': [90, 79, 75, 99, 97]}
frame = pd.DataFrame(data)
frame


# In[103]:


# set our index 
pd.DataFrame(data, columns=['Popular', 'Programming', 'Year'])


# In[133]:


data2 = pd.DataFrame(data, columns=['Year', 'Programming', 'Popular', 'Users'],
                    index=[1,2,3,4,5])
data2


# In[134]:


data2['Programming']


# In[135]:


data2.Popular


# In[137]:


data2.Users = np.random.random(5)*104
data2 = np.round(data2)
data2


# #### How to combine two data set using pandas?

# In[169]:


# we will do merging two dataset together 
merg1 = {'Edit': 24, 'View': 11, 'Inser': 18, 'Cell': 40}
merg1 = pd.Series(merg1)
merg1 = pd.DataFrame(merg1, columns=['Merge1'])

merg2 = {'Kernel':50, 'Navigate':27, 'Widgets':29,'Help':43}
merg2 = pd.Series(merg2)
merg2 = pd.DataFrame(merg2, columns=['Merge2'])


# In[170]:


merg1


# In[171]:


merg2


# In[195]:


#join matching rows from bdf to adf
#pd.merge(merg1, merg2, left_index=True, right_index=True)
join = merg1.join(merg2)
join


# In[199]:


#replace all NA/null data with value
join = join.fillna(12)
join


# In[201]:


#compute and append one or more new columns
join = join.assign(Area=lambda df: join.Merge1*join.Merge2)
join


# In[205]:


#add single column
join['Volume'] = join.Merge1*join.Merge2*join.Area
join


# In[209]:


join.head(2)


# In[208]:


join.tail(2)


# In[210]:


#randomly select fraction of rows
join.sample(frac=0.5)


# In[211]:


#order rows by values of a column (low to high)
join.sort_values('Volume')


# In[213]:


#order row by values of a column (high to low)
join.sort_values('Volume', ascending=False)


# In[217]:


#return the columns of a dataframe - by renaming
join = join.rename(columns={'Merge1':'X','Merge2':'Y'})


# In[218]:


join


# In[220]:


#count number of rows with each unique value of variable
join['Y'].value_counts()


# In[221]:


#number of rows in dataframe
len(join)


# In[222]:


#descriptive statistics
join.describe()


# ### Thank you, more to come soon!
