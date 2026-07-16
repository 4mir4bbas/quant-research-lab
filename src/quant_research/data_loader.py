from pathlib import Path

import pandas as pd
import yfinance as yf


def download_market_data(
    ticker: str,
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """Download historical market data for a ticker."""

    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False,
    )

    if data.empty:
        raise ValueError(f"No data was returned for ticker: {ticker}")

    return data


def save_market_data(data: pd.DataFrame, ticker: str) -> Path:
    """Save market data as a CSV file."""

    output_directory = Path("data/raw")
    output_directory.mkdir(parents=True, exist_ok=True)

    output_path = output_directory / f"{ticker.lower()}.csv"
    data.to_csv(output_path)

    return output_path