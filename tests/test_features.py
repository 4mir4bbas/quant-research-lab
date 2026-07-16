import pandas as pd
import pytest

from src.quant_research.features import add_return_features


def test_add_return_features() -> None:
    data = pd.DataFrame(
        {
            "Close": [100.0, 101.0, 99.0, 102.0],
        }
    )

    result = add_return_features(data)

    assert "daily_return" in result.columns
    assert "volatility_20d" in result.columns
    assert pd.isna(result.loc[0, "daily_return"])
    assert result.loc[1, "daily_return"] == pytest.approx(0.01)


def test_add_return_features_requires_close_column() -> None:
    data = pd.DataFrame(
        {
            "Open": [100.0, 101.0],
        }
    )

    with pytest.raises(ValueError, match="Close"):
        add_return_features(data)