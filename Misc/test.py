import plotly.graph_objects as go 
import yfinance as yf 
import pandas as np 
import numpy as np 
import datetime as dt 
import matplotlib.pyplot as plt 
import requests

#%matplotlib inline
print('libraries imported')

# Set the start and end date
start_date = '2023-5-01'
end_date = '2024-2-17'
 
# Set the ticker
ticker = 'smci'
 
# Get the data
data = yf.download(ticker, start_date, end_date)
 
# Print the last 5 rows
#print(data.tail())


copydf=data.copy()
#the original data has Data as index, for plotly lib, have to convert Data from index as a normal column
copydf.reset_index(level=0, inplace=True)
df=copydf 
print(df.head(100))
#df.to_csv("smci.csv")
#df.to_excel("smci.xlsx", sheet_name="data_history")

'''
ticker = yf.Ticker('GOOGL').info
print(ticker.keys())
print(ticker['ask'])
print(ticker['shortPercentOfFloat'])
'''

def get_borrow_data(ticker):
    #https://iborrowdesk.com/api/ticker/LEO
    print(f"in get borrow data for {ticker}")

    url = "https://iborrowdesk.com/api/ticker/" + ticker.upper()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)

    if not r.ok:
        print('request failure in get_borrow_data')
        print(r)
    try:
        result = r.json()['daily']
        return result[-10:]
    except Exception as e:
        print('error in get_borrow_data')
        print(e)

b = get_borrow_data("smci")
print(b)