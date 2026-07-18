import pandas as pd
import pytest

from src.quant_research.strategy import (
    add_moving_average_strategy,
)


def test_add_moving_average_strategy() -> None:
    data = pd.DataFrame(
        {
            "Close": [
                100.0,
                101.0,
                102.0,
                103.0,
                104.0,
                105.0,
            ],
            "daily_return": [
                0.0,
                0.01,
                0.0099,
                0.0098,
                0.0097,
                0.0096,
            ],
        }
    )

    result = add_moving_average_strategy(
        data,
        short_window=2,
        long_window=3,
    )

    expected_columns = {
        "short_ma",
        "long_ma",
        "signal",
        "position",
        "strategy_return",
        "buy_hold_equity",
        "strategy_equity",
    }

    assert expected_columns.issubset(result.columns)
    assert result.loc[2, "signal"] == 1
    assert result.loc[2, "position"] == 0
    assert result.loc[3, "position"] == 1


def test_strategy_rejects_invalid_windows() -> None:
    data = pd.DataFrame(
        {
            "Close": [100.0, 101.0],
            "daily_return": [0.0, 0.01],
        }
    )

    with pytest.raises(
        ValueError,
        match="short_window",
    ):
        add_moving_average_strategy(
            data,
            short_window=20,
            long_window=10,
        )


def test_strategy_requires_expected_columns() -> None:
    data = pd.DataFrame(
        {
            "Close": [100.0, 101.0],
        }
    )

    with pytest.raises(
        ValueError,
        match="daily_return",
    ):
        add_moving_average_strategy(data)