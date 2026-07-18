from src.quant_research.data_loader import (
    download_market_data,
    save_market_data,
    save_processed_data,
)
from src.quant_research.features import add_return_features

from src.quant_research.strategy import (
    add_moving_average_strategy,
)

from src.quant_research.visualization import (
    save_cumulative_return_chart,
    save_price_chart,
    save_volatility_chart,
    save_moving_average_chart,
    save_strategy_equity_chart
)




def main() -> None:
    ticker = "SPY"

    raw_data = download_market_data(
        ticker=ticker,
        start_date="2020-01-01",
        end_date="2025-01-01",
    )

    featured_data = add_return_features(raw_data)

    strategy_data = add_moving_average_strategy(
        featured_data,
        short_window=50,
        long_window=200,
    )
    
    raw_path = save_market_data(raw_data, ticker)
    processed_path = save_processed_data(strategy_data, ticker)
    price_chart_path = save_price_chart(strategy_data, ticker)
    cumulative_chart_path = save_cumulative_return_chart(
        strategy_data,
        ticker,
    )
    volatility_chart_path = save_volatility_chart(
        strategy_data,
        ticker,
    )

    moving_average_chart_path = save_moving_average_chart(
        strategy_data,
        ticker,
    )
    strategy_chart_path = save_strategy_equity_chart(
        strategy_data,
        ticker,
    )



    print(f"Downloaded {len(raw_data)} rows for {ticker}.")
    print(f"Saved raw data to: {raw_path}")
    print(f"Saved processed data to: {processed_path}")
    print(f"Saved price chart to: {price_chart_path}")
    print(f"Saved cumulative return chart to: {cumulative_chart_path}")
    print(f"Saved volatility chart to: {volatility_chart_path}")
    print(
        "Saved moving-average chart to: "
        f"{moving_average_chart_path}"
    )
    print(
        "Saved strategy comparison chart to: "
        f"{strategy_chart_path}"
    )

if __name__ == "__main__":
    main()