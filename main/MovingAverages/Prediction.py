import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.mlab as mlab
import math
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf,pacf
import statsmodels.tsa.stattools as ts
from statsmodels.tsa.arima_model import ARIMA
from pandas.tools.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_pacf



data = pd.read_csv("GoogleStock.csv")
print(data)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date',inplace=True)
close = data['Close']
lnclose = np.log(close)
plt.plot(lnclose)
plt.show()
acf_1 = acf(lnclose)[1:20]
test_df = pd.DataFrame([acf_1]).T
test_df.columns = ['Partial Correlation']
test_df.index +=1
test_df.plot(kind='bar')
plt.show()
pacf_1 = pacf(lnclose)[1:20]
test_pacf = pd.DataFrame([pacf_1]).T
test_pacf.columns = ['Partial Correlattion']
test_pacf.index += 1
test_pacf.plot(kind= 'bar')
plt.show()

price_matrix = lnclose.as_matrix()
model = ARIMA(price_matrix,order=(0,1,0))
model_fit = model.fit(disp = 0)
print(model_fit.summary())

predictions = model_fit.predict(2518,2524,typ= 'levels')
print(predictions)
predictions_adj = np.exp(predictions)
print(predictions)
plt.plot(predictions)
plt.show()
plt.plot(predictions_adj)
plt.show()
#----------------------------------------
# print(data.index)
# data.plot
# close = data['Close']
# close.rolling(100).mean().plot(label =  '100 days rolling mean ')
# close.plot
# plt.show()
# autocorrelation_plot(close)
# plt.show()
#
# model = ARIMA(close, order=(777,1,2))
# model_fit =  model.fit()
#---------------------------------
# new_data = data.set_index('Date')
# new_data['Date'] = pd.to_datetime(new_data['Date'])
# print(new_data)
# close = new_data['Close']
# print(close.head(5))
# start_date =datetime.strptime('2007-01-03', '%Y-%m-%d')
# end_date = datetime.strptime('2017-01-01', '%Y-%m-%d')
# all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
# # close = close.reindex(all_weekdays)
# print(close.head(10))
# print(close.describe())
