import pandas as pd

from src.quant_research.visualization import (
    save_cumulative_return_chart,
    save_price_chart,
    save_volatility_chart,
    save_moving_average_chart,
    save_strategy_equity_chart,
)


def test_visualizations_are_saved(
    tmp_path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)

    index = pd.date_range(
        start="2025-01-01",
        periods=3,
        freq="D",
    )

    data = pd.DataFrame(
        {
            "Close": [100.0, 101.0, 102.0],
            "cumulative_return": [0.0, 0.01, 0.02],
            "volatility_20d": [0.1, 0.12, 0.11],
            "short_ma": [100.0, 100.5, 101.5],
            "long_ma": [100.0, 100.3, 101.0],
            "buy_hold_equity": [1.0, 1.01, 1.02],
            "strategy_equity": [1.0, 1.0, 1.01],
        },
        index=index,
    )

    price_path = save_price_chart(data, "TEST")
    cumulative_path = save_cumulative_return_chart(
        data,
        "TEST",
    )
    volatility_path = save_volatility_chart(
        data,
        "TEST",
    )

    moving_average_path = save_moving_average_chart(
        data,
        "TEST",
    )

    strategy_path = save_strategy_equity_chart(
        data,
        "TEST",
    )

    assert price_path.exists()
    assert cumulative_path.exists()
    assert volatility_path.exists()
    assert moving_average_path.exists()
    assert strategy_path.exists()