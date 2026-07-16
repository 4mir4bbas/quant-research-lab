from src.quant_research.main import main


def test_main_runs(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert "Quant Research Lab is ready." in captured.out
