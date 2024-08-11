import pandas as pd

class Backtester:
    def run(self, model, data, rebalance_frequency='M'):
        returns = data.pct_change().dropna()
        portfolio_returns = pd.Series(index=returns.index)
        
        for start, end in zip(returns.index[::22], returns.index[22::22]):  # Monthly rebalancing
            weights = model.optimize_portfolio()
            period_returns = returns.loc[start:end]
            portfolio_returns.loc[start:end] = (period_returns * weights).sum(axis=1)
        
        return portfolio_returns
