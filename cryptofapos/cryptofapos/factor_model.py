import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class FactorModel:
    def extract_factors(self, data):
        returns = data.pct_change().dropna()
        
        # Market factor
        market_cap = data * self._get_market_cap(data)
        market_factor = (market_cap * returns).sum(axis=1) / market_cap.sum(axis=1)
        
        # Size factor
        log_market_cap = np.log(market_cap)
        size_factor = log_market_cap.rank(axis=1, pct=True)
        
        # Momentum factor
        momentum = returns.rolling(window=22).sum()
        momentum_factor = momentum.rank(axis=1, pct=True)
        
        return pd.DataFrame({
            'Market': market_factor,
            'Size': size_factor.mean(axis=1),
            'Momentum': momentum_factor.mean(axis=1)
        })

    def _get_market_cap(self, data):
        # Placeholder for market cap data
        return pd.DataFrame(np.random.randn(*data.shape), index=data.index, columns=data.columns)

    def estimate_exposures(self, data, factors):
        returns = data.pct_change().dropna()
        exposures = pd.DataFrame(index=returns.columns, columns=factors.columns)
        
        for crypto in returns.columns:
            model = LinearRegression()
            model.fit(factors, returns[crypto])
            exposures.loc[crypto] = model.coef_
        
        return exposures
