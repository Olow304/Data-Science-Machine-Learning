
# coding: utf-8

# ## Model fitting
# * Supervised Learning
# * Unsupervised Learning

# ### supervised learning model fitting

# In[1]:


from sklearn.datasets import load_iris
holder = load_iris()
X, y = holder.data, holder.target


# In[7]:


#supervised learning model fitting with linearRegression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)


# In[8]:


from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state =0)


# In[9]:


#supervised learning model fitting with Kneighbor classifier
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)


# In[10]:


#supervised learning model fitting with support vector classifier
from sklearn.svm import SVC
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)


# ### unsupervised learning model fitting

# In[11]:


#unsupervised learning model fitting with kmeans
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3, random_state=0)
k_means.fit(X_train)


# In[12]:


#unsupervised learning model fitting with PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=0.95)
pca_model = pca.fit_transform(X_train)

