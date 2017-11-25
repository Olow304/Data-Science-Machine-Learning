#Mean Absolute Error
from sklearn.metrics import mean_absolute_error
y_true = [3, -0.5, 2]
mean_absolute_error(y_true, y_pred)

#mean squared error
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)

#Rsquare Score
from sklearn.metrics import r2_score
r2_score(y_true, y_pred)
