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
        multi_level_index=False,
    )

    if data.empty:
        raise ValueError(f"No data was returned for ticker: {ticker}")

    data = normalize_market_data(data)

    return data


def normalize_market_data(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """Convert downloaded market data to flat columns."""

    result = data.copy()

    if isinstance(result.columns, pd.MultiIndex):
        result.columns = result.columns.get_level_values(0)

    result.index.name = "Date"

    return result


def save_market_data(data: pd.DataFrame, ticker: str) -> Path:
    """Save market data as a CSV file."""

    output_directory = Path("data/raw")
    output_directory.mkdir(parents=True, exist_ok=True)

    output_path = output_directory / f"{ticker.lower()}.csv"
    data.to_csv(output_path)

    return output_path


def save_processed_data(data: pd.DataFrame, ticker: str) -> Path:
    """Save processed market data as a CSV file."""

    output_directory = Path("data/processed")
    output_directory.mkdir(parents=True, exist_ok=True)

    output_path = output_directory / f"{ticker.lower()}_features.csv"
    data.to_csv(output_path)

    return output_path