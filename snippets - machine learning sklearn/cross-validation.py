from sklearn.cross_validation import cross_val_score
print(cross_val_score(knn, X_train, y_train, cv = 5))
print(cross_val_score(lr, X, y, cv = 4))
