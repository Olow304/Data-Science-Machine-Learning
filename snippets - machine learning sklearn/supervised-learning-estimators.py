#LinearRegression
from sklearn.linear_model import LinearRegression
lr = LinearRegression(normalize=True)

#Support Vector Machine (SVM)
from sklearn.svm import SVC
svc = SVC(kernel='linear')

#Naive Bayes
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

#K Nearest Neighbors
from sklearn import neighbors 
knn = neighbors.KNeighborsClassifier(n_neighbors=5)