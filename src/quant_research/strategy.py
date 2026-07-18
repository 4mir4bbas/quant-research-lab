import pandas as pd


def add_moving_average_strategy(
    data: pd.DataFrame,
    short_window: int = 50,
    long_window: int = 200,
) -> pd.DataFrame:
    """Add a long-only moving-average crossover strategy."""

    required_columns = {"Close", "daily_return"}
    missing_columns = required_columns.difference(data.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(
            f"Input data is missing required columns: {missing}"
        )

    if short_window <= 0 or long_window <= 0:
        raise ValueError("Moving-average windows must be positive.")

    if short_window >= long_window:
        raise ValueError(
            "short_window must be smaller than long_window."
        )

    result = data.copy()

    result["short_ma"] = (
        result["Close"]
        .rolling(window=short_window)
        .mean()
    )

    result["long_ma"] = (
        result["Close"]
        .rolling(window=long_window)
        .mean()
    )

    result["signal"] = (
        result["short_ma"] > result["long_ma"]
    ).astype(int)

    result["position"] = result["signal"].shift(1).fillna(0)

    result["strategy_return"] = (
        result["position"] * result["daily_return"]
    )

    result["buy_hold_equity"] = (
        1 + result["daily_return"].fillna(0)
    ).cumprod()

    result["strategy_equity"] = (
        1 + result["strategy_return"].fillna(0)
    ).cumprod()

    return result