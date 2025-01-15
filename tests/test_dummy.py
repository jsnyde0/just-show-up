import pytest


@pytest.mark.skip(reason="This is a dummy test")
def test_dummy():
    """A simple test to verify pytest is working."""
    expected = True
    actual = True
    assert actual == expected, "Basic assertion should pass"


def test_dummy2():
    """A simple test to verify pytest is working."""
    expected = True
    actual = True
    assert actual == expected, "Basic assertion should pass"
