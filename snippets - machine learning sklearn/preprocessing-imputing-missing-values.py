from sklearn.preprocessing import Imputer
impute = Imputer(missing_values = 0, strategy='mean', axis=0)
impute.fit_transform(X_train)