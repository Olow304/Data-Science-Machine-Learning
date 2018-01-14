# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 11:29:24 2017

@author: Saleban
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA, ARIMAResults
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pylab as plt
import matplotlib.dates as dates
from matplotlib.pylab import rcParams

dataMaster = pd.read_csv('new_data.csv')
data = dataMaster['United States']
print(data.head(12))

ran = pd.date_range('1995-01', '2016-1', freq = 'M')
ts = pd.Series(dataMaster['United States'].values, index = ran)
print(ts.head(12))
print(ts.dtypes)

plt.plot(ts)
plt.title('How home prices in the US has changed over time')
#plt.xlim([0, 255])
plt.xlabel('Year')
plt.ylabel('Price $')
plt.show()
sp500_TR = ts['1995':'2014']
print(sp500_TR)

acf = plot_acf(ts, lags = 20)
plt.title("ACF Plot of SP 500")
acf.show()
pacf = plot_pacf(ts, lags = 20)
plt.title("PACF Plot of SP 500")
pacf.show()

# TRANSFORMING OUR DATA TO ADJUST FOR NON-STATIONARITY
sp500_diff = ts - ts.shift()
diff = sp500_diff.dropna()
print(diff.head(12))
print(diff.dtypes)

plt.figure()
plt.plot(diff)
plt.title('First Difference Time Series Plot')
plt.show()

acfDiff = plot_acf(diff, lags = 20)
plt.title("ACF Plot of S 500(Difference)")
acfDiff.savefig("images/timeSeriesACFDiff.png", format = 'png')
acfDiff.show()

# edit this shit on the actual project !
pacfDiff = plot_pacf(diff, lags = 20)
plt.title("PACF Plot of SP 500(Difference)")
pacfDiff.savefig("images/pacfDiff.png", format = 'png')
pacfDiff.show()

mod = ARIMA(sp500_TR, order = (0, 2, 1), freq = 'M')
results = mod.fit()
print(results.summary())

predVals = results.predict(139, 291, typ='levels')
print(predVals)

predVals = predVals.drop(predVals.index[0])
print(predVals)

sp500_for = pd.concat([ts, predVals], axis = 1, keys=['original', 'predicted'])
print(sp500_for['2014':'2018'])

plt.figure()
plt.plot(sp500_for)
plt.title("Actual Vs. Forecasted Values")
plt.savefig("images/sp500_for.png", format = 'png')
plt.show()

plt.figure()
plt.plot(sp500_for)
plt.title('Real Vs. Predicted Values for May 2017 and beyond')
plt.savefig("images/sp500_for2.png", format = 'png')
plt.show()




