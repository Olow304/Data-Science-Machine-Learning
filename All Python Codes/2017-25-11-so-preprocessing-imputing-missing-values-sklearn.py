
# coding: utf-8

# ## Imputing missing values in sklearn
# 
# Mean imputation replaces missing values with the mean value of that feature/variable. Mean imputation is one of the most 'naive' imputation methods because unlike more complex methods like k-nearest neighbors imputation, it does not use the information we have about an observation to estimate a value for it.

# In[1]:


import warnings
warnings.filterwarnings('ignore')


# In[2]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer


# In[12]:


# Create an empty dataset
df = pd.DataFrame()

# Create two variables called x0 and x1. Make the first value of x1 a missing value
df['x0'] = [0.3051,0.4949,0.6974,np.nan,0.2231,np.nan,0.4436,0.5897,0.6308,0.5]
df['x1'] = [np.nan,0.2654,0.2615,0.5846,0.4615,np.nan,0.4962,0.3269,np.nan,0.6731]

# View the dataset
df


# In[18]:


# Create an imputer object that looks for 'Nan' values
mean_imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)

# Train the imputor on the df dataset
mean_imputer = mean_imputer.fit(df)


# In[19]:


# Apply the imputer to the df dataset
imputed_df = mean_imputer.transform(df.values)

