import yfinance as yf

class DataLoader:
    def __init__(self, crypto_tickers, start_date, end_date):
        self.tickers = crypto_tickers
        self.start_date = start_date
        self.end_date = end_date

    def load_data(self):
        data = yf.download(self.tickers, start=self.start_date, end=self.end_date)
        return data['Adj Close']
