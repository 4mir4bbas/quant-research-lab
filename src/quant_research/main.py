from src.quant_research.data_loader import (
    download_market_data,
    save_market_data,
    save_processed_data,
)
from src.quant_research.features import add_return_features

from src.quant_research.visualization import (
    save_cumulative_return_chart,
    save_price_chart,
    save_volatility_chart,
)


def main() -> None:
    ticker = "SPY"

    raw_data = download_market_data(
        ticker=ticker,
        start_date="2020-01-01",
        end_date="2025-01-01",
    )

    featured_data = add_return_features(raw_data)

    
    raw_path = save_market_data(raw_data, ticker)
    processed_path = save_processed_data(featured_data, ticker)

    price_chart_path = save_price_chart(featured_data, ticker)
    cumulative_chart_path = save_cumulative_return_chart(
        featured_data,
        ticker,
    )
    volatility_chart_path = save_volatility_chart(
        featured_data,
        ticker,
    )



    print(f"Downloaded {len(raw_data)} rows for {ticker}.")
    print(f"Saved raw data to: {raw_path}")
    print(f"Saved processed data to: {processed_path}")
    print(f"Saved price chart to: {price_chart_path}")
    print(f"Saved cumulative return chart to: {cumulative_chart_path}")
    print(f"Saved volatility chart to: {volatility_chart_path}")


if __name__ == "__main__":
    main()