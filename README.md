# CryptoFAPOS

CryptoFAPOS (Cryptocurrency Factor Analytics and Portfolio Optimization System) is a Python library for factor-based cryptocurrency investment and risk management.

## Features

- Factor extraction (market, size, momentum)
- Dynamic factor exposure estimation
- Portfolio optimization with factor tilts
- Risk management and backtesting

## Installation

pip install cryptofapos

## Quick Start

from cryptofapos import CryptoFAPOS

crypto_tickers = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'BCH-USD']
cfapos = CryptoFAPOS(crypto_tickers, '2018-01-01', '2023-01-01')

factors = cfapos.extract_factors()
exposures = cfapos.estimate_factor_exposures()
weights = cfapos.optimize_portfolio(risk_aversion=1, factor_tilts={'Market': 1, 'Size': 0.2, 'Momentum': 0.3})
returns = cfapos.backtest()
metrics = cfapos.calculate_performance_metrics(returns)

print("Optimal weights:", weights)
print("Performance metrics:", metrics)
