import sys

from lab_02_01_json_processing.main import (
    display_orders,
    display_summary,
    main,
    run_menu,
)


def test_display_orders(sample_orders, capsys):
    display_orders(sample_orders)

    output = capsys.readouterr().out

    assert "Juan Perez" in output
    assert "Laptop" in output
    assert "$30,000.00" in output


def test_display_empty_orders(capsys):
    display_orders([])

    assert "No orders found." in capsys.readouterr().out


def test_display_summary(sample_orders, capsys):
    display_summary(sample_orders)

    output = capsys.readouterr().out

    assert "Total orders: 5" in output
    assert "Completed sales: $36,000.00" in output


def test_menu_exit(sample_orders, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")

    run_menu(sample_orders)

    assert "Goodbye!" in capsys.readouterr().out


def test_menu_invalid_option(sample_orders, monkeypatch, capsys):
    inputs = iter(["99", "0"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    run_menu(sample_orders)

    output = capsys.readouterr().out

    assert "Invalid option" in output
    assert "Goodbye!" in output


def test_main_missing_file(tmp_path, monkeypatch, capsys):
    file_path = tmp_path / "missing.json"

    monkeypatch.setattr(
        sys,
        "argv",
        ["orders", str(file_path)],
    )

    result = main()

    assert result == 1
    assert "Application error" in capsys.readouterr().err
