import numpy as np
import pandas as pd
from scipy.optimize import minimize

class PortfolioOptimizer:
    def optimize(self, data, factor_exposures, risk_aversion=1, factor_tilts=None):
        returns = data.pct_change().dropna()
        mean_returns = returns.mean()
        cov_matrix = returns.cov()
        
        def objective(weights):
            portfolio_return = np.sum(mean_returns * weights)
            portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            factor_exposure = np.dot(factor_exposures.T, weights)
            factor_tilt_penalty = 0
            if factor_tilts is not None:
                factor_tilt_penalty = np.sum((factor_exposure - factor_tilts)**2)
            return -portfolio_return + risk_aversion * portfolio_risk + factor_tilt_penalty

        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for _ in range(len(data.columns)))
        
        initial_weights = np.array([1/len(data.columns)] * len(data.columns))
        result = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
        
        return pd.Series(result.x, index=data.columns)
