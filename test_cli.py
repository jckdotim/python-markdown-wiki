from click.testing import CliRunner
from cli import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'createdb' in result.output
    assert 'dropdb' in result.output
