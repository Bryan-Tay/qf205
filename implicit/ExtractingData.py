import pandas as pd
from datetime import date, timedelta
from pandas_datareader import data as wb
import numpy as np

date_one_year_ago = date.today() - timedelta(days=365)

d0 = date.today()
d1 = date(1970,1,1) #yahoo finance starts their period count from 1 Jan 1970
d2 = d0-d1
d3 = (d2.days)*86400 #60s * 60min * 24h = 1 day in seconds
d4 = d3-(86400*365) #Period count 1 year ago

def stock_price(ticker):
    prices = pd.read_html(f'https://finance.yahoo.com/quote/{ticker}/history?p={ticker}')
    p = prices[0]
    price_now = float(p.iloc[0,5])
    return price_now

def rf_rate():
    rate = pd.read_html('https://finance.yahoo.com/quote/^TNX?p=^TNX')
    r = rate[0]
    rate_now = float(r.iloc[0,1]/100)
    return rate_now

def historical_dividends(ticker):
    while True:
        try:
            histdivs = pd.read_html(f'https://finance.yahoo.com/quote/{ticker}/history?period1={d4}&period2={d3}&interval=div%7Csplit&filter=div&frequency=1mo')
            histdivs=histdivs[0]
            histdivs.drop(histdivs.tail(1).index,inplace=True)
            histdivs.drop(columns = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4',
                            'Unnamed: 5', 'Unnamed: 6'], inplace= True)
            histdivs['Dividends']= histdivs['Dividends'].apply(lambda x: x.replace('Dividend',''))
            histdivs['Dividends']= histdivs['Dividends'].astype(float)
            histdivs['Date'] = pd.to_datetime(histdivs['Date'])
            return histdivs
        except KeyError:
            return ""

def dividend_yield(ticker):
    while True:
        try:
            divs = historical_dividends(ticker)
            curdiv = divs['Dividends'][0]
            numerator = curdiv*4 #annualizing current dividends
            price_now = stock_price(ticker)
            dyr=numerator/price_now
            return dyr
            break
        except TypeError:
            return 0
        
def sd(ticker):
    prices = pd.DataFrame(wb.get_data_yahoo(ticker,date_one_year_ago,interval = 'd')['Adj Close'])
    hist_r = ((prices['Adj Close']/prices['Adj Close'].shift(-1))-1)
    ave_r = hist_r.mean()
    variance = (((hist_r-ave_r)**2).sum()/(len(hist_r)-1))*250 #annualising variance after calculating variance per day
    sd = np.sqrt(variance)
    return sd
