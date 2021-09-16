from matplotlib import style
from mpl_finance import candlestick_ohlc
import mplfinance as mpf
import matplotlib.dates as mdates
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2020, 9, 13)
stock_name = 'MBBM.KL'
data_source = 'yahoo'

#Download stock data from web
# df = web.DataReader(name=stock_name, data_source=data_source, start=start, end=end)    #access data from server
# df.to_csv('MAYBANK.csv')    #download it as csv

#Read CSV file
df = pd.read_csv('MAYBANK.csv', parse_dates=True, index_col=0)
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()
df_ohlc.reset_index(inplace=True)
df_ohlc['Date']=df_ohlc['Date'].map(mdates.date2num)

#mpf.plot(df,type='candle') ;todo: use default library
#print('default data:\n', df.head())
#print('\ndf_ohlc data:\n', df_ohlc.head())
#print('\ndf_volume:\n', df_volume.head())

# Plot graph
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
#ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])
plt.show()
