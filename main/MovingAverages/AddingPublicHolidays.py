
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import yahoo_historical
from datetime import datetime


dataModel = yahoo_historical.Fetcher('GOOGL',[2017,1,3], [2019,1,5])

data  = dataModel.getHistorical()
print(data.tail(5))

data['Date'] = pd.to_datetime(data.Date)
data = data.set_index('Date')
print(data.tail(5))

start_date =datetime.strptime('2017-01-03', '%Y-%m-%d')
end_date = datetime.strptime('2019-01-06', '%Y-%m-%d')

all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')


data = data.reindex(all_weekdays)
print(data.tail(5))




# data = data.reindex(all_weekdays)
# print(data)


