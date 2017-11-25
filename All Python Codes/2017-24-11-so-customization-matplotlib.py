
# coding: utf-8

# ## Working with Matplotlib
# Introduction:
# 
# Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shell, the jupyter notebook, web application servers, and four graphical user interface toolkits.
# 
# ### Here are the main steps we will go through
# * How to save your plot using matplotlib?
# * How to create plot using matplotlib?
# * How to make your graph look pretty?
# 
# This is Just a little illustration.
# 
# <img style="float:left;" src="https://static.lwn.net/images/2015/02-matplotlib-3d.png"></img>

# #### How to save your plot using matplotlib?
# I am gonna show you how to save your graph, you can refer the docstring for complete information on the various ways it can be used.

# In[1]:


# import matplotlib, numpy
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


#saves plot/figure to image
plt.savefig('name_your_graph.png')


# In[11]:


# we can create simple plot as follows, linear graph
# Prepare the data
linear = np.linspace(0, 10, 100)

# Plot the data, set label and color, b=blue, g=green
plt.plot(linear, linear, label='linear', color='b')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[23]:


#by calling 
plt.style.available


# In[26]:


x = np.linspace(0, 4 * np.pi)
y = np.sin(x)

plt.plot(x, y)

plt.show()


# In[27]:


plt.style.use('ggplot')

plt.plot(x, y)

plt.show()


# In[32]:


with plt.style.context(('seaborn-darkgrid')):
    plt.plot(x, y, 'r-o')
    plt.show()


# #### Working with text inside your graph

# However, you can use subplots to set up and place your Axes on a regular grid. So that means that in most cases, Axes and subplot are synonymous, they will designate the same thing. When you do call subplot to add Axes to your figure, do so with the add_subplots() function. 

# In[14]:


# we can create scatter plot for this 
fig = plt.figure()

# Set up Axes
ax = fig.add_subplot(111)

# Scatter the data
ax.scatter(np.linspace(0, 1, 5), np.linspace(0, 5, 5), label='scatter')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# #### How To Change The Size of Figures
# 
# Now that you have seen how to initialize a Figure and Axes from scratch, you will also want to know how you can change certain small details that the package sets up for you, such as the figure size.
# Let’s say you don’t to have your figure size to be default size and you want to change this. How do you set the size of your figures manually?

# In[20]:


# easy! you can just call 
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)


# In[21]:


# let's plot simple bar graph
# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])

# Show the plot
plt.show()


# In[3]:


x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()


# In[4]:


#plot data connected by lines
lines = plt.plot(x,x)
plt.show()


# ## More to come soon!
