import pandas as pd


def add_return_features(data: pd.DataFrame) -> pd.DataFrame:
    """Add daily return and rolling volatility features."""

    if "Close" not in data.columns:
        raise ValueError("Input data must contain a 'Close' column.")

    result = data.copy()

    result["daily_return"] = result["Close"].pct_change()

    result["cumulative_return"] = (
        1 + result["daily_return"].fillna(0)
    ).cumprod() - 1

    result["volatility_20d"] = (
        result["daily_return"]
        .rolling(window=20)
        .std()
        * (252**0.5)
    )

    return result