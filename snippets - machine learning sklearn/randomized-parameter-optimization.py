from sklearn.grid_search import RandomizedSearchCV
params = {"n_neighbors" : range(1,5),
		  "weights": ["uniform", "distance"]}
rsearch = RandomizedSearchCV(estimator=knn,
							 param_distributions=params,
							 cv=4,
							 n_iter=8,
							 random_state=5)
rsearch.fit(X_train, y_train)
print(rsearch.best_score_)