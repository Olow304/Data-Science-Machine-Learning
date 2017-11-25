import pandas as pd 

#specify with start date and number of periods
rng = pd.date_range('2017 Jul 15 10:13',
					periods=10, freq='M')

#add timestamp
pd.Timestamp('2017-07-10')
#or
pd.Timestamp('2017-07-10 10:15:13.999')

#convert between a DateTimeIndex and a PeriodIndex
ts_dt.to_period()	# convert to periodIndex
ts_pd.to_timestamp()# convert to dataTimeIndex

#runing time
import timeit
#always use %timeit before calling command
%timeit data = pd.read()

#data resampling
_data = pd.date_range('1/1/2011', periods=72, freq='H')
ts = pd.Series(list(range(len(_data))), index=_data)
ts.head()
 
#only access every 45 minutes
converted = ts.asfreq('45Min', method='ffill')
