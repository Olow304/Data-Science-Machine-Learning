
# coding: utf-8

# # Bar plots in Matplotlib

# In[5]:


get_ipython().magic('pylab')
get_ipython().magic('matplotlib inline')


# In[17]:


# input data
mean_values = [3.3, 1, 2, 3]
variance = [0.3,0.2, 0.4, 0.5]
bar_labels = ['bar 1', 'bar 2', 'bar 3','bar 4']

# plot bars
x_pos = list(range(len(bar_labels)))
bar(x_pos, mean_values)

# set height of the y-axis
max_y = max(zip(mean_values, variance)) # returns a tuple, here: (3, 5)
ylim([0, (max_y[0] + max_y[1]) * 1.1])

# set axes labels and title
ylabel('Y lable')
xticks(x_pos, bar_labels)
title('Bar plot')


# In[90]:


# input data
figure(figsize=(10,5))
mean_values = [3.3, 1, 2, 3]
variance = [0.3,0.2, 0.4, 0.5]
bar_labels = ['bar 1', 'bar 2', 'bar 3','bar 4']

# plot bars
x_pos = list(range(len(bar_labels)))
barh(x_pos, mean_values,align='center', alpha=0.4, color='g')

# set height of the y-axis
max_y = max(zip(mean_values, variance)) 
ylim([len(max_y)+0.5])
# set axes labels and title
ylabel('Y lable')
xticks(x_pos, bar_labels)
title('Bar plot')


# In[39]:


# Input data
green_data = [1, 3, 5]
blue_data = [4, 2, 3.4]
red_data = [3, 4, 6]
labels = ['Green', 'Blue', 'Red']

# Setting the positions and width for the bars
pos = list(range(len(green_data))) 
width = 0.2 
    
# Plotting the bars
fig, ax = subplots(figsize=(8,6))

bar(pos, green_data, width, alpha=0.5, color='g', label=labels[0])
bar([p + width for p in pos], blue_data, width, alpha=0.5, color='b', label=labels[1])
bar([p + width*2 for p in pos], red_data, width, alpha=0.5, color='r', label=labels[2])

# Setting axis labels and ticks
ax.set_ylabel('y-value')
ax.set_title('Grouped bar plot')
ax.set_xticks([p + 1.5 * width for p in pos])
ax.set_xticklabels(labels)

# Setting the x-axis and y-axis limits
xlim(min(pos)-width, max(pos)+width*4)
ylim([0, max(green_data + blue_data + red_data) * 1.5])

# Adding the legend and showing the plot
legend(['Green', 'Blue', 'Red'], loc='upper left')


# In[86]:


data = range(200, 225, 5)

bar_labels = ['a', 'b', 'c', 'd', 'e']

fig = figure(figsize=(10,8))

# plot bars
y_pos = np.arange(len(data))
yticks(y_pos, bar_labels, fontsize=12)
bars = barh(y_pos, data, align='center', alpha=0.5, color='g')

# annotation and labels
for b,d in zip(bars, data):
    text(b.get_width() + b.get_width()*0.05, b.get_y() + b.get_height()/2,
        '{0:.0%}'.format(d/min(data)), 
        ha='center', va='bottom', fontsize=12, color='k')

xlabel('X axis label', fontsize=12)
ylabel('Y axis label', fontsize=12)
t = title('Bar plot with plot labels/text', fontsize=14)
ylim([-1,len(data)+0.5])
vlines(min(data), -1, len(data)+0.5, linestyles='--', color='r')

