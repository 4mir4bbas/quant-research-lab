from src.quant_research.data_loader import (
    download_market_data,
    save_market_data,
)


def main() -> None:
    ticker = "SPY"

    data = download_market_data(
        ticker=ticker,
        start_date="2020-01-01",
        end_date="2025-01-01",
    )

    output_path = save_market_data(data, ticker)

    print(f"Downloaded {len(data)} rows for {ticker}.")
    print(f"Saved data to: {output_path}")


if __name__ == "__main__":
    main()