import plotly.graph_objects as go 
import yfinance as yf 
import pandas as pd
import numpy as np 
import datetime as dt 
#import matplotlib.pyplot as plt 
from openpyxl import load_workbook
import xlsxwriter

aapl = yf.Ticker("aapl")
print(aapl)
#print(aapl.income_stmt)
#print(type(aapl.income_stmt))
'''
print(aapl.news)
print(aapl.quarterly_income_stmt)
print(aapl.balance_sheet)
print(aapl.cashflow)
print(aapl.quarterly_cashflow)

print(aapl.major_holders)
print(aapl.institutional_holders)
print(aapl.mutualfund_holders)

print(aapl.insider_transactions)
print(aapl.insider_purchases)
print(aapl.insider_roster_holders)

print(aapl.recommendations)
print(aapl.recommendations_summary)
print(aapl.upgrades_downgrades)
print(aapl.insider_roster_holders)

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
print(aapl.earnings_dates)
print(aapl.isin)


print(aapl.get_shares_full(start="2024-01-01", end=None))

# get historical market data
hist = aapl.history(period="1mo")

# show meta information about the history (requires history() to be called first)
print(aapl.history_metadata)
'''
def auto_width_columns(df, sheetname):
        workbook = writer.book  
        worksheet= writer.sheets[sheetname] 
    
        for i, col in enumerate(df.columns):
            column_len = max(df[col].astype(str).str.len().max(), len(col) + 2)
            worksheet.set_column(i, i, column_len)


path='smci.xlsx'
writer = pd.ExcelWriter(path, engine = 'openpyxl', mode='a', if_sheet_exists='replace')#xlsxwriter'


x3 = np.random.randn(100, 2)
df3  = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice a Long Name'], # this is a very long name
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
})
x4 = np.random.randn(100, 2)
df4 = pd.DataFrame(x4)


df3.to_excel(writer, sheet_name = 'x3', index=True)
df4.to_excel(writer, sheet_name = 'x4', index=True)
#sheet_report = writer.sheets["x3"]  # Access sheet
#sheet_report.set_column(1, 1, 15)  # Modify column widths


writer.close()


ticker=yf.Ticker('smci')
ticker_content=ticker.income_stmt 
for col in ticker_content.columns:
    print (col)
    if col in list(ticker_content.columns):
         print("yes")
    
print(type(list(ticker_content.columns)))
print(ticker_content.columns.tolist)



