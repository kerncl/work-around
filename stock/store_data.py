import investpy
import pandas as pd
import numpy as np

MY = 'Malaysia'
MCO = '09/03/2020'   # MCO start date
midMCO = '15/06/2020'   # Covid 19 2 digit
CMCO = '07/07/2020'     # CMCO start date

df = investpy.get_stocks(country=MY)
# df.to_csv('malaysia_stock_list.csv') # export list of malaysia company into csv
M_stock_list = df[['symbol','name']].set_index('symbol')
stock_data = {}
for stock in M_stock_list.index:
    # print(investpy.get_stock_recent_data(stock=stock, country=MY))
    try:
        price_list = investpy.get_stock_historical_data(stock=stock, country=MY, from_date=MCO, to_date=CMCO)['Close'].tolist()
        stock_data[stock] = max(price_list) - min(price_list)
    except:
        print(stock)
print(stock_data)
# print(df)
# print(M_stock_list)