from src.quant_research.data_loader import (
    download_market_data,
    save_market_data,
    save_processed_data,
)
from src.quant_research.features import add_return_features


def main() -> None:
    ticker = "SPY"

    data = download_market_data(
        ticker=ticker,
        start_date="2020-01-01",
        end_date="2025-01-01",
    )

    featured_data = add_return_features(data)

    
    raw_path = save_market_data(data, ticker)
    processed_path = save_processed_data(featured_data, ticker)

    print(f"Saved raw data to: {raw_path}")
    print(f"Saved processed data to: {processed_path}")
    print(featured_data.tail())


if __name__ == "__main__":
    main()