#! usr/local/bin/python3 

"""
The class to devleop various functions for single stock symbol
"""

import plotly.graph_objects as go 
import yfinance as yf 
import pandas as pd 
import numpy as np 
import datetime as dt 
import matplotlib.pyplot as plt 

#from datetime import timedelta, datetime
#delta = timedelta(days=-300)# I need 300 days history data

##cache 
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache"),
)

#%matplotlib inline
print('libraries imported')

class SingleStock: 
    def __init__(self, ticker):
        self.ticker =ticker
        self.start_data = "2025-1-1"  
        self.end_data="2025-2-16"
        self.excel_sheet_name=['para','summary','price_history', 'borrowing_info','income_statement','quarter_income_statement','balance_sheet', 'cashflow', 'quarter_cashflow', 'trans_N_rate']
        #end = datetime.datetime.today()  
        #start = datetime.date(end.year-2,1,1)

    def download_data(self, intraday='1d'):
        '''
        input 
            start_data and end_data: str format; 2023-01-01 
        output:
            ticket data in dataframe 
        #Obtain adjusted data, which accounts for stock splits, dividends, etc.
        range of interval: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        
        usage: 
        download_data()
        download_data("1wk")
        ''' 
        #data=yf.download(self.ticker , self.start_data, self.end_data)  #, auto_adjust=True
        #with below option, the dataframe show two mores columns
        data=yf.download(self.ticker , self.start_data, self.end_data, interval=intraday)
        #return data.loc[:, ~data.columns.isin(['Dividends','Stock Splits'])] 
        print(data)
        #print(data.loc[:, ~data.columns.isin(['Dividends','Stock Splits'])] )

    def display_ticker_last_n_days_data(self,n=5):
        '''
        the original data has Data as index, for plotly lib, have to convert Data from index as a normal column
        input 
            n: integer, number of data to be displayed
        output: 
            last n data of tick in dataframe
        '''
        copydf=self.download_data().copy()
        copydf.reset_index(level=0, inplace=True)
        df=copydf 
        #print(df.head(100)) #default is 5
        #print(df.tail(n))
        return df.tail(n)
    
    def display_ticker_info(self, *arg):
        '''
        input: either No input or "key" 
        output: 
            display either ticker's full information or key information 
        '''
        ticker_dict_content= yf.Ticker(self.ticker)
        print(type(ticker_dict_content.info))
        if len(arg) == 0:
            for key, value in ticker_dict_content.info.items():
                print(key,":",value)
        elif len(arg) == 1 and arg[0] == 'key':
            #print(ticker_dict_content.info['dividendYield'])
            print("Company Symbol : "+ str(ticker_dict_content.info["symbol"]) + 
                "\t(" + str(ticker_dict_content.info["industry"]) + ")" + 
                "\tMarket Cap: "+ str(ticker_dict_content.info["marketCap"]))
            print("=" * 60 + "\n")

            print("trailingPE(TTM): "+ str(ticker_dict_content.info["trailingPE"])+ 
                "\tforwardPE(FWD): "+ str(ticker_dict_content.info["forwardPE"])+ 
                "\ttrailingEps(TTM): "+ str(ticker_dict_content.info["trailingEps"])+ 
                "\tforwardEps(TTM): "+ str(ticker_dict_content.info["forwardEps"]))
            print("earningsQuarterlyGrowth: "+ str(ticker_dict_content.info["earningsQuarterlyGrowth"])+ "\n")

            print("currentPrice : "+ str(ticker_dict_content.info["currentPrice"])+ "\t")
            print("targetHighPrice: "+ str(ticker_dict_content.info["targetHighPrice"])+ "\t")
            print("targetLowPrice : "+ str(ticker_dict_content.info["targetLowPrice"])+ "\t")
            print("targetMeanPrice : "+ str(ticker_dict_content.info["targetMeanPrice"])+ "\t")
            print("recommendationMean: "+ str(ticker_dict_content.info["recommendationMean"])+ "\t")
            print("recommendationKey: "+ str(ticker_dict_content.info["recommendationKey"])+ "\t")
            print("numberOfAnalystOpinions : "+ str(ticker_dict_content.info["numberOfAnalystOpinions"])+ "\n")
            
            print("fiftyTwoWeekLow: "+ str(ticker_dict_content.info["fiftyTwoWeekLow"])+ "\t")
            print("fiftyTwoWeekHigh: "+ str(ticker_dict_content.info["fiftyTwoWeekHigh"])+ "\t")
            print("twoHundredDayAverage: "+ str(ticker_dict_content.info["twoHundredDayAverage"])+ "\t")
            print("52WeekChange: "+ str(ticker_dict_content.info["52WeekChange"])+ "\n")

            print("profitMargins: "+ str(ticker_dict_content.info["profitMargins"])+ "\n")

            print("sharesShort: "+ str(ticker_dict_content.info["sharesShort"])+ "\n")
            print("sharesShortPriorMonth: "+ str(ticker_dict_content.info["sharesShortPriorMonth"])+ "\n")
            print("sharesShortPreviousMonthDate: "+ str(ticker_dict_content.info["sharesShortPreviousMonthDate"])+ "\n")
            print("shortRatio: "+ str(ticker_dict_content.info["shortRatio"])+ "\n")
            print("shortPercentOfFloat: "+ str(ticker_dict_content.info["shortPercentOfFloat"])+ "\n")

            print("totalCashPerShare  : "+ str(ticker_dict_content.info["totalCashPerShare"])+ "\n")
            print("quickRatio  : "+ str(ticker_dict_content.info["quickRatio"])+ "\n")
            print("currentRatio : "+ str(ticker_dict_content.info["currentRatio"])+ "\n")
            print("revenuePerShare : "+ str(ticker_dict_content.info["revenuePerShare"])+ "\n")
            print("freeCashflow: "+ str(ticker_dict_content.info["freeCashflow"])+ "\n")
            print("earningsGrowth  : "+ str(ticker_dict_content.info["earningsGrowth"])+ "\n")
            print("revenueGrowth  : "+ str(ticker_dict_content.info["revenueGrowth"])+ "\n")
            print("grossMargins  : "+ str(ticker_dict_content.info["grossMargins"])+ "\n")
            print("revenuePerEmployee : "+ str(ticker_dict_content.info["totalRevenue"]/ticker_dict_content.info["fullTimeEmployees"])+ "\n")

    '''CSV and Excel'''
    def ticker_price_data_to_csv(self):
        '''
        convert the ticker price history to csv format
        '''
        df= self.download_data()
        file_name=self.ticker
        df.to_csv(f"{file_name}.csv")

    def store_ticker_price_data_to_excel(self, sh_name): 
        '''
        convert ticker price data to excel format at sheet name 
        '''
        df= self.download_data()
        file_name=self.ticker
        if sh_name in self.excel_sheet_name:
            idx=self.excel_sheet_name.index(sh_name)
            df.to_excel(f"{file_name}.xlsx", sheet_name=self.excel_sheet_name[idx])
    
    def store_ticker_finance_to_excel(self, sh_name):
        '''
        store ticker's finance data to excel by sheet name
        validated input for sheet_name=
        ['income_statement','quarter_income_statement','balance_sheet', 'cashflow', 'quarter_cashflow', 'trans_N_rate']

        '''
        dict ={'income_statement':'income_stmt'}

        ticker=yf.Ticker(self.ticker)
        file_name=self.ticker 
        if sh_name in self.excel_sheet_name:
            attr=dict[sh_name]
            #print(type(attr))
            ticker_content=ticker.income_stmt  #dataframe

            idx=self.excel_sheet_name.index(sh_name)
            #print(ticker_content)
            #without below command, to_excel will override instead of append
            writer=pd.ExcelWriter(f"{file_name}.xlsx", engine='openpyxl', mode='a', if_sheet_exists='replace')
            #to keep index, index=True
            ticker_content.to_excel(writer, sheet_name=self.excel_sheet_name[idx], index=True)  
            writer.close()
  
    def excel_data_to_dataframe(self,sh_name):
        '''
        input: 
        sh_name: one of element in self.excel_sheet_name
        output: 
        return dataframe conversion from corresponding sheet name of excel
        '''
        file_name=self.ticker
        if sh_name in self.excel_sheet_name:
            idx=self.excel_sheet_name.index(sh_name)
            excel_data_df = pd.read_excel(f"{file_name}.xlsx",sheet_name=[self.excel_sheet_name[idx]])
            return excel_data_df
        else: 
            print("Wrong input. Try again")
    
    '''Dividen and Stock Split'''
    def dividen_and_stock_split(self):
        ticker_dict_content= yf.Ticker(self.ticker)
        print(ticker_dict_content.actions)
        #print(len(ticker_dict_content.dividends))
        #print(ticker_dict_content.dividends)
        #print(len(ticker_dict_content.splits))
        #print(ticker_dict_content.splits)
    '''Call_put_option'''
    def option_expiry_date(self):
        ticker_content = yf.Ticker(self.ticker)
        return ticker_content.option 

    def call_option(self, date):
        ticker_content = yf.Ticker(self.ticker)
        if date in ticker_content.option:
            call_opt_data=ticker_content.option_chain(date)
            return call_opt_data.calls 
        else: 
            print("invalidated date. Try again")

    def put_option(self, date):
        ticker_content = yf.Ticker(self.ticker)
        if date in ticker_content.option:
            call_opt_data=ticker_content.option_chain(date)
            return call_opt_data.puts
        else: 
            print("invalidated date. Try again") 
                    
    '''Graph Section'''
    def plot_ticker_candlestick_graph(self):
        '''
        plot candlestick graph for ticker
        '''
        copydf=self.download_data().copy()
        copydf.reset_index(level=0, inplace=True)
        df=copydf 
        fig=go.Figure(data=[go.Candlestick(x=df['Date'],
              open=df['Open'],
              high=df['High'],
              low=df['Low'],
              close=df['Close'])])     
        fig.show() 

    def simple_moving_average(self, *arg):
        '''
        input: 
            integer
        output: 
            plot graph with simple moving average
        usage: 
            simple_moving_average(3)
            simple_moving_average(3,5)
            simple_moving_average(3,5,15)
        '''
        data = self.download_data()
        if len(arg) == 0 or len(arg) > 3:
            print("not validation")

        data[str(arg[0])] = data['Adj Close'].rolling(arg[0]).mean()
        if len(arg) == 2: 
            data[str(arg[1])] = data['Adj Close'].rolling(arg[1]).mean()
            
        if len(arg) == 3: 
            data[str(arg[1])] = data['Adj Close'].rolling(arg[1]).mean()
            data[str(arg[2])] = data['Adj Close'].rolling(arg[2]).mean()
        plt.rcParams["figure.figsize"]=(18,10)
        plt.plot(data[str(arg[0])], label="SMA" + str(arg[0]), color='red', linewidth=1)
        if len(arg) == 2:     
            plt.plot(data[str(arg[1])],label="SMA" + str(arg[1]), color='blue',linewidth=1)
            
        if len(arg) == 3:     
            plt.plot(data[str(arg[1])],label="SMA" + str(arg[1]), color='blue',linewidth=1)
            plt.plot(data[str(arg[2])],label="SMA" + str(arg[2]), color='green',linewidth=1)
        plt.plot(data['Adj Close'], label='Adj Close', color='black',linewidth=1)
        plt.legend(loc='upper left')
        plt.title(self.ticker)
        plt.show()


    '''Validation Section'''
    def function_validate(self):
        #1 download_data() validation
        res_dd= self.download_data()
        print(res_dd.tail())
        print(type(res_dd))
    
        #2 display_ticker_last_n_days_data() valition
        res_dtlndd = self.display_ticker_last_n_days_data(10)
        print(res_dtlndd)

        #3 plot cadble graph
        self.plot_ticker_candlestick_graph()

        #4 simple moving graph
        self.simple_moving_average(3)
        self.simple_moving_average(3,5)
        self.simple_moving_average(3,5,15)

        # csv and excel 
        self.ticker_price_data_to_csv()
        self.ticker_price_data_to_excel()


def main(): 
    #self.excel_sheet_name=['price_history', 'borrowing_info','income_statement','quarter_income_statement','balance_sheet', 'cashflow', 'quarter_cashflow', 'trans_N_rate']

    res_ss= SingleStock("nvda")
    print(res_ss.ticker)

    res_dd=res_ss.download_data()
    #print(res_dd.tail())
    #print(type(res_dd))
    #print(res_dd.keys())
    #res_ss.display_ticker_info('key')
    #res_ss.ticker_price_data_to_csv()
    
    #a = res_ss.excel_data_to_dataframe('price_history')
    #print(a)
    #print("=="*40)
    #b= res_ss.excel_data_to_dataframe('income_statment')
    #print(b)
    
    #res_ss.store_ticker_finance_to_excel('income_statement')
    
    #res_ss.store_ticker_price_data_to_excel('price_history')

    '''
    res_dtlndd = res_ss.display_ticker_last_n_days_data()
    print(res_dtlndd)

    res_ss.plot_ticker_candlestick_graph()

    #res_ss.simple_moving_average(3)
    res_ss.simple_moving_average(3,5)
    res_ss.simple_moving_average(3,5,15)
    '''

if  __name__ == '__main__':
    main()
    #data = yf.download("AAPL", start="2024-07-01", end="2024-07-31")
    #print(data.head())
