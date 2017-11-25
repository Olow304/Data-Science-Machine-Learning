#supervised learning model fitting
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)

from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

from sklearn.svm import SVC
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)

#unsupervised learning model fitting
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3, random_state=0)
k_means.fit(X_train)

from sklearn.decomposition import PCA
pca = PCA(n_components=0.95)
pca_model = pca.fit_transform(X_train)