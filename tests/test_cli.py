# tests/test_cli.py
from click.testing import CliRunner
import src.cli as cli
import src.store as store

def test_cli_add_and_list(tmp_path, monkeypatch):
    file = tmp_path / "data.json"
    store.DATA_FILE = str(file)
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["add", "hello"])
    assert result.exit_code == 0
    assert "Added: hello" in result.output

    result = runner.invoke(cli.cli, ["list"])
    assert result.exit_code == 0
    assert "1." in result.output
    assert "hello" in result.output

def test_cli_done_invalid(tmp_path):
    file = tmp_path / "data.json"
    store.DATA_FILE = str(file)
    runner = CliRunner()
    # mark done when no items -> should error
    result = runner.invoke(cli.cli, ["done", "1"])
    assert result.exit_code != 0