from .data_loader import DataLoader
from .factor_model import FactorModel
from .portfolio_optimizer import PortfolioOptimizer
from .risk_manager import RiskManager
from .backtester import Backtester

class CryptoFAPOS:
    def __init__(self, crypto_tickers, start_date, end_date):
        self.data_loader = DataLoader(crypto_tickers, start_date, end_date)
        self.factor_model = FactorModel()
        self.portfolio_optimizer = PortfolioOptimizer()
        self.risk_manager = RiskManager()
        self.backtester = Backtester()

    def extract_factors(self):
        data = self.data_loader.load_data()
        return self.factor_model.extract_factors(data)

    def estimate_factor_exposures(self):
        data = self.data_loader.load_data()
        factors = self.factor_model.extract_factors(data)
        return self.factor_model.estimate_exposures(data, factors)

    def optimize_portfolio(self, risk_aversion=1, factor_tilts=None):
        data = self.data_loader.load_data()
        factors = self.factor_model.extract_factors(data)
        exposures = self.factor_model.estimate_exposures(data, factors)
        return self.portfolio_optimizer.optimize(data, exposures, risk_aversion, factor_tilts)

    def backtest(self, rebalance_frequency='M'):
        data = self.data_loader.load_data()
        return self.backtester.run(self, data, rebalance_frequency)

    def calculate_performance_metrics(self, returns):
        return self.risk_manager.calculate_metrics(returns)
