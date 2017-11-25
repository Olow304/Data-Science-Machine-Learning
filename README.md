# Complete-Data-Science-Toolkits
The overall objective of this toolkit is to provide and offer a free collection of data analysis and machine learning that is specifically suited for doing data science. Its purpose is to get you started in a matter of minutes. You can run this collections either in Jupyter notebook, python alone or the html version.
# Features
## Machine Learning
* Cross-Validation
* Evaluating Classification Metrics
* Evaluating Clustering Metrics
* Evaluating Regression Metrics
* Grid Search
* Preprocessing Encoding Categorical Features
* Preprocessing Binarization
* Preprocessing Imputing Missing Values
* Preprocessing Normalization
* Preprocessing StandardScaler
* Randomized Parameter Optimization
## Numpy 
* Adding, Removing, and Splitting Arrays
* Sorting arrays
* Matrix object
* Statistics Vector Math
* Structured Arrays
* Import, Export, Slicing, Indexing
* Data to from string
## Pandas
* Complete pandas 
* Groupby in Pandas
* Mapping
* Filtering
* Applying
## Visualization
* BarPlots 
* Customization Matplotlib
* Working with Image
* Working with text 

# Naming Conventions
* The naming convections I followed is: 
* <b>[yyyy-mm-dd-in-project-name-library].extention</b>
* <b>yyyy</b> = stands for year
* <b>mm</b> = stands for month
* <b>dd</b> = stands for day
* <b>in</b> = my initial, for example: Saleban Olow = so
* <b>library</b> = numpy, pandas, sklearn, matplotlib
* <b>project-name</b> = each project name
* <b>extention</b> = .ipynb, .py, .html
* Example: <i>2017-25-11-so-cross-validation-sklearn.ipynb</i>

# Code Samples:

> Cross Validation
```python
from sklearn.model_selection import cross_val_score
model = SVC(kernel='linear', C=1)
# let's try it using cv
scores = cross_val_score(model, X, y, cv=5)
```
***
> Grid Search
```python
from sklearn.grid_search import GridSearchCV
params = {"n_neighbors": np.arange(1,5), "metric": ["euclidean", "cityblock"]}
grid = GridSearchCV(estimator=knn, param_grid=params)
grid.fit(X_train, y_train)
print(grid.best_score)
print(grid.best_estimator_.n_neighbors)
```
***
> Preprocessing Imputing Missing Values
```python
from sklearn.preprocessing import Imputer
impute = Imputer(missing_values = 0, strategy='mean', axis=0)
impute.fit_transform(X_train)
```
***
> Randomized Parameter Optimization
```python
from sklearn.grid_search import RandomizedSearchCV
params = {"n_neighbors" : range(1,5), "weights": ["uniform", "distance"]}
rsearch = RandomizedSearchCV(estimator=knn, param_distributions=params, cv=4, n_iter=8, random_state=5)
rsearch.fit(X_train, y_train)
print(rsearch.best_score_)
```
***
> Model fitting supervised and unsupervised learning
```python
#supervised learning
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
#unsupervised learning
from sklearn.decomposition import PCA
pca = PCA(n_components=0.95)
pca_model = pca.fit_transform(X_train)
```
***
> Working with numpy arrays
```python
import numpy as np 
#appends values to end of arr
np.append(arr, values)
#inserts values into arr before index 2
np.insert(arr, 2, values)
```
***
> Indexing and Slicing arrays
```python
import numpy as np 
#return the element at index 5
arr = np.array([[1,2,3,4,5,6,7]])
arr[5]
#returns the 2D array element on index 
arr[2,5]
#assign array element on index 1 the value 4
arr[1] = 4
#assign array element on index [1][3] the value 10
arr[1,3] = 10
```
***
> Creating DataFrame
```python
import pandas as pd 
#specify values for each rows and columns
df = pd.DataFrame(
	[[4,7,10],
	 [5,8,11],
	 [6,9,12]],
	 index=[1,2,3],
	 columns=['a','b','c'])
```
***
> groupby pandas
```python
import pandas as pd 
import pandas as pd 
#return a groupby object, grouped by values in column named 'cities'
df.groupby(by="Cities")
```
***
> handling missing values
```python
import pandas as pd 
#drop rows with any column having NA/null data.
df.dropna()
#replace all NA/null data with value
df.fillna(value)
```
***
> Melt function
```python
import pandas as pd 
#most pandas methods return a DataFrame so that
#this improves readability of code
df = (pd.melt(df)
	  .rename(columns={'old_name':'new_name', 'old_name':'new_name'})
	  .query('new_name >= 200')
)
```
***
> Save plot 
```python
mport matplotlib.pyplot as plt 
#saves plot/figure to image
plt.savefig('pic_name.png')
```
***
> Marker, lines
```python
import matplotlib.pyplot as plt 
#add * for every data point
plt.plot(x,y, marker='*')
#adds dot for every data point
plt.plot(x,y, marker='.')
```
***
> Figures, Axis
```python
import matplotlib.pyplot as plt 
#a container that contains all plot elements
fig = plt.figures()
#Initializes subplot
fig.add_axes()
#A subplot is an axes on a grid system, rows-cols num
a = fig.add_subplot(222)
#adds subplot
fig, b = plt.subplots(nrows=3, ncols=2)
#creates subplot
ax = plt.subplots(2,2)
```
***
> Working with text plot
```python
import matplotlib.pyplot as plt 
#places text at coordinates 1/1
plt.text(1,1, 'Example text', style='italic')
#annotate the point with coordinates xy with text 
ax.annotate('some annotation', xy=(10,10))
#just put math formula
plt.title(r'$delta_i=20$',fontsize=10)
```
***
