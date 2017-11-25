
# coding: utf-8

# ## Evaluating Clustering Metrics
# 
# ### Main contents:
# * adjusted rand index
# * homogeneity
# * V-measure

# ### Rand index adjusted for chance.
# The Rand Index computes a similarity measure between two clusterings by considering all pairs of samples and counting pairs that are assigned in the same or different clusters in the predicted and true clusterings.

# In[1]:


from sklearn.metrics import adjusted_rand_score
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
adjusted_rand_score(y_true, y_pred)


# In[2]:


adjusted_rand_score([0, 0, 1, 2], [0, 0, 1, 1])  


# In[3]:


adjusted_rand_score([0, 0, 0, 0], [0, 1, 2, 3])


# ### Homogeneity
# Homogeneity metric of a cluster labeling given a ground truth.
# A clustering result satisfies homogeneity if all of its clusters contain only data points which are members of a single class.

# In[4]:


from sklearn.metrics.cluster import homogeneity_score
homogeneity_score([0, 0, 1, 1], [1, 1, 0, 0])


# In[5]:


print("%.6f" % homogeneity_score([0, 0, 1, 1], [0, 0, 1, 2]))
print("%.6f" % homogeneity_score([0, 0, 1, 1], [0, 1, 2, 3]))


# In[7]:


print("%.6f" % homogeneity_score([0, 0, 1, 1], [0, 1, 0, 1]))                                               
print("%.6f" % homogeneity_score([0, 0, 1, 1], [0, 0, 0, 0]))
# you can just play around testing different data points                                                


# ### V-measure
# V-measure cluster labeling given a ground truth.
# This score is identical to normalized_mutual_info_score.
# 
# The V-measure is the harmonic mean between homogeneity and completeness:
# v = 2 * (homogeneity * completeness) / (homogeneity + completeness)
# 
# This metric is independent of the absolute values of the labels: a permutation of the class or cluster label values won’t change the score value in any way.
# 
# This metric is furthermore symmetric: switching label_true with label_pred will return the same score value. This can be useful to measure the agreement of two independent label assignments strategies on the same dataset when the real ground truth is not known.

# In[8]:


from sklearn.metrics.cluster import v_measure_score
v_measure_score([0, 0, 1, 1], [0, 0, 1, 1])
v_measure_score([0, 0, 1, 1], [1, 1, 0, 0])


# In[9]:


print("%.6f" % v_measure_score([0, 0, 1, 2], [0, 0, 1, 1]))
print("%.6f" % v_measure_score([0, 1, 2, 3], [0, 0, 1, 1]))


# In[10]:


print("%.6f" % v_measure_score([0, 0, 0, 0], [0, 1, 2, 3]))

