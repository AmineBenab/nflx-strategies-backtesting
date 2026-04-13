import pandas as pd
import numpy as np

def rend_cum(returns):
    return np.exp(returns.sum()) - 1

def rend_annu(returns, periods):
    return (1 + rend_cum(returns)) ** (periods / len(returns)) - 1

def rend_mean(returns):
    return (1 / len(returns)) * returns.sum()

def vol_period(returns):
    return returns.std()

def vol_annu(returns, periods):
    return vol_period(returns) * np.sqrt(periods)

def sharpe(returns, periods):
    return rend_annu(returns, periods) / vol_annu(returns, periods)

def max_drawdown(equity):
    return min((equity - equity.cummax()) / equity.cummax())

def sortino(returns, periods):
    down = returns[returns < 0]
    return rend_annu(returns, periods) / vol_annu(down, periods)

def calmar(returns, equity, periods):
    return rend_annu(returns, periods) / abs(max_drawdown(equity))

def winrate(returns):
    return (returns > 0).sum() / len(returns)

def var_hist(returns):
    return np.percentile(returns.dropna(), 5)

def cond_var_hist(returns):
    return returns[returns < var_hist(returns)].mean()

def drawdown(equity):
    return (equity - equity.cummax()) / equity.cummax()

def compute_metrics(returns, equity, freq="monthly"):
    if freq == "monthly":
        periods = 12
    elif freq == "daily":
        periods = 252
    elif isinstance(freq, int):
        periods = freq

    return pd.Series({
        "Cumulative return":        f"{rend_cum(returns):.2%}",
        "Annualized return":        f"{rend_annu(returns, periods):.2%}",
        "Mean return":              f"{rend_mean(returns):.2%}",
        "Period volatility":        f"{vol_period(returns):.2%}",
        "Annual volatility":        f"{vol_annu(returns, periods):.2%}",
        "Winrate":                  f"{winrate(returns):.2%}",
        "Sharpe Ratio":             f"{sharpe(returns, periods):.4f}",
        "Max Drawdown":             f"{max_drawdown(equity):.2%}",
        "Sortino":                  f"{sortino(returns, periods):.4f}",
        "Calmar":                   f"{calmar(returns, equity, periods):.4f}",
        "Historic VaR":             f"{var_hist(returns):.2%}",
        "Conditional Historic VaR": f"{cond_var_hist(returns):.2%}"
    })