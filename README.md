# NFLX Trading Strategies Backtesting
A personal project comparing multiple portfolio strategies on Netflix (NFLX) stock, built with Python and Jupyter Notebook.

## Overview
This project implements and compares five trading strategies on historical NFLX data, evaluating their risk-adjusted performance through a standardized set of metrics. The framework is fully reusable and can be applied to any stock or ETF by opening `Data_loading.ipynb` and changing the ticker. Prices are based on adjusted closing prices.
All equity curves are normalized to a starting value of $1,000 and filtered from 2019-01-31 for clarity and comparability across strategies.

## Strategies
| Strategy | Frequency | Purpose |
|---|---|---|
| Buy & Hold | Daily | Passive long-term exposure |
| Momentum | Monthly | Follow the trend |
| SMA Crossover (50/200) | Daily | Trend following |
| Volatility Targeting | Daily | Dynamic risk management |
| Mean Reversion (Bollinger Bands) | Daily | Revert to the mean |


## Performance Metrics
Each strategy is evaluated using `compute_metrics()` from `Fonctions.py` :

- Cumulative & Annualized Return
- Mean Return & Volatility (Period & Annual)
- Sharpe Ratio
- Sortino Ratio
- Calmar Ratio
- Max Drawdown
- Winrate
- Historic VaR & Conditional VaR (CVaR)

## Project Structure
```
├── Fonctions.py                  # Reusable metrics and utility functions
├── Data_loading.ipynb            # Data download and preprocessing
├── Buy_And_Hold.ipynb
├── Momentum.ipynb
├── SMA Crossover.ipynb
├── Volatility Targeting.ipynb
├── Mean_Reversion.ipynb
├── Final_Comparison.ipynb        # Comparative metrics table
├── NFLX_data.csv                 # Raw price data
├── NFLX_data_return.csv          # Log-returns
└── metrics_*.csv                 # Exported metrics per strategy
```
## Requirements
numpy
pandas
matplotlib

## Usage

1. Clone the repository
2. Install dependencies : `pip install numpy pandas matplotlib`
3. Run each strategy notebook independently
4. Run `Final_Comparison.ipynb` for the full comparison table

## Key Results

Backtesting period : 2019 - 2024

| Strategy | Annualized Return | Sharpe Ratio | Max Drawdown |
|---|---|---|---|
| Momentum | 29.44% | 1.07 | -38.12% |
| SMA Crossover | 18.46% | 0.54 | -48.00% |
| Volatility Target | 12.16% | 0.35 | -65.17% |
| Mean Reversion | 5.82% | 0.38 | -34.52% |
