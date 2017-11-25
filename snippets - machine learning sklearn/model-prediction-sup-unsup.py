#supervised learning model prediction
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
y_pred = lr.predict(X_test)

from sklearn.svm import SVC
svc = SVC(kernel='linear')
y_pred = svc.predict(np.random.random((2,5)))

from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
y_pred = knn.predict_proba(X_test)

#unsupervised learning model prediction
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3, random_state=0)
y_pred = k_means.predict(X_test)
