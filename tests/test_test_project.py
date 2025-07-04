"""Basic tests for test-project."""


def test_import() -> None:
    """Test that the package can be imported."""
    import test_project
    assert hasattr(test_project, '__version__')


def test_version() -> None:
    """Test that version is defined."""
    from test_project import __version__
    assert __version__ is not None
    assert isinstance(__version__, str)
