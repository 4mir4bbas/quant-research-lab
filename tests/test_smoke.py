import pandas as pd

from src.quant_research.data_loader import save_market_data


def test_save_market_data(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)

    data = pd.DataFrame(
        {
            "Close": [100.0, 101.0, 102.0],
        }
    )

    output_path = save_market_data(data, "TEST")

    assert output_path.exists()
    assert output_path.name == "test.csv"