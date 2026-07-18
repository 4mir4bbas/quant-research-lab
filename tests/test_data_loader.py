import pandas as pd

from src.quant_research.data_loader import (
    normalize_market_data,
)


def test_normalize_market_data_flattens_multiindex() -> None:
    columns = pd.MultiIndex.from_tuples(
        [
            ("Close", "SPY"),
            ("High", "SPY"),
            ("Volume", "SPY"),
        ]
    )

    data = pd.DataFrame(
        [
            [100.0, 101.0, 1_000_000],
            [102.0, 103.0, 1_100_000],
        ],
        columns=columns,
    )

    result = normalize_market_data(data)

    assert list(result.columns) == [
        "Close",
        "High",
        "Volume",
    ]


