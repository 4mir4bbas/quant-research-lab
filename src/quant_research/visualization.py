from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_price_chart(data: pd.DataFrame, ticker: str) -> Path:
    """Create and save a closing-price chart."""

    if "Close" not in data.columns:
        raise ValueError("Input data must contain a 'Close' column.")

    output_directory = Path("outputs/figures")
    output_directory.mkdir(parents=True, exist_ok=True)

    output_path = output_directory / f"{ticker.lower()}_price.png"

    figure, axis = plt.subplots(figsize=(12, 6))

    axis.plot(data.index, data["Close"])
    axis.set_title(f"{ticker} Adjusted Closing Price")
    axis.set_xlabel("Date")
    axis.set_ylabel("Price")
    axis.grid(alpha=0.3)

    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt.close(figure)

    return output_path


def save_cumulative_return_chart(
        data: pd.DataFrame,
        ticker: str,
) -> Path:
    """Create and save a cumulative-return chart."""

    if "cumulative_return" not in data.columns:
        raise ValueError(
            "Input data must contain a 'cumulative_return' column."
        )

    output_directory = Path("outputs/figures")
    output_directory.mkdir(parents=True, exist_ok=True)

    output_path = (
        output_directory
        / f"{ticker.lower()}_cumulative_return.png"
    )
    figure, axis = plt.subplots(figsize=(12, 6))

    axis.plot(data.index, data["cumulative_return"])
    axis.set_title(f"{ticker} Cumulative Return")
    axis.set_xlabel("Date")
    axis.set_ylabel("Cumulative Return")
    axis.grid(alpha=0.3)

    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt.close(figure)

    return output_path


def save_volatility_chart(
    data: pd.DataFrame,
    ticker: str,
) -> Path:
    """Create and save a rolling-volatility chart."""

    if "volatility_20d" not in data.columns:
        raise ValueError(
            "Input data must contain a 'volatility_20d' column."
        )

    output_directory = Path("outputs/figures")
    output_directory.mkdir(parents=True, exist_ok=True)

    output_path = (
        output_directory
        / f"{ticker.lower()}_volatility.png"
    )

    figure, axis = plt.subplots(figsize=(12, 6))

    axis.plot(data.index, data["volatility_20d"])
    axis.set_title(f"{ticker} 20-Day Annualized Volatility")
    axis.set_xlabel("Date")
    axis.set_ylabel("Annualized Volatility")
    axis.grid(alpha=0.3)

    figure.tight_layout()
    figure.savefig(output_path, dpi=150)
    plt.close(figure)

    return output_path