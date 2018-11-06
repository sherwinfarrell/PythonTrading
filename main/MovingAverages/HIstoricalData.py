import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import yahoo_historical
from datetime import datetime
dataModel = yahoo_historical.Fetcher('GOOGL',[2007,1,1], [2017,1,1])

data  = dataModel.getHistorical()
print(data)
print(data.head(5))
data.to_csv("GoogleStock.csv",index=None)

# close = data['Close']
# print(close.head(5))
# start_date =datetime.strptime('2007-01-03', '%Y-%m-%d')
# end_date = datetime.strptime('2017-01-01', '%Y-%m-%d')
# all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
#
#
# print(close.head(5))