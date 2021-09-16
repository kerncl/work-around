import csv
import datetime
path = 'google_stock_data.csv'
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader) #print using generator extract the first line
#data = [row for row in reader]
#lines = [line.strip().split(',') for line in open(path)]

data = []
for row in reader:
    #row = [Date, Open, High, Low, Close, Volume, Adj. Close]
    date = row[0]
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    data.append([date, open_price, high, low, close, volume, adj_close])

#Compute and store daily stock returns
return_path = 'google_returns.csv'
file= open(return_path, 'w')
writer= csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data)-1):
    todays_row = data[1]
    todays_date= todays_row[0]
    todays_price= todays_row[-1]
    yesterday_row = data[i+1]
    yesterday_price= yesterday_row[-1]
    daily_return = (todays_price-yesterday_price)/ yesterday_price
    writer.writerow([todays_date, daily_return])
