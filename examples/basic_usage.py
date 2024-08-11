from cryptofapos import CryptoFAPOS

def main():
    crypto_tickers = ['BTC-USD', 'ETH-USD', 'XRP-USD', 'LTC-USD', 'BCH-USD']
    cfapos = CryptoFAPOS(crypto_tickers, '2018-01-01', '2023-01-01')

    factors = cfapos.extract_factors()
    print("Extracted factors:")
    print(factors.head())

    exposures = cfapos.estimate_factor_exposures()
    print("\nFactor exposures:")
    print(exposures)

    weights = cfapos.optimize_portfolio(risk_aversion=1, factor_tilts={'Market': 1, 'Size': 0.2, 'Momentum': 0.3})
    print("\nOptimal weights:")
    print(weights)

    returns = cfapos.backtest()
    print("\nBacktest returns:")
    print(returns.head())

    metrics = cfapos.calculate_performance_metrics(returns)
    print("\nPerformance metrics:")
    print(metrics)

if __name__ == "__main__":
    main()
