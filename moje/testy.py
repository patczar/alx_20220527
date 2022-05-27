import pytest


@pytest.fixture
def miasta():
    return ["Warszawa", "Kraków"]


def test1(miasta):
    assert "Warszawa" in miasta

