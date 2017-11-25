from sklearn.grid_search import GridSearchCV
params = {"n_neighbors": np.arange(1,5),
		  "metric": ["euclidean", "cityblock"]}
grid = GridSearchCV(estimator=knn, param_grid=params)
grid.fit(X_train, y_train)
print(grid.best_score)
print(grid.best_estimator_.n_neighbors)

