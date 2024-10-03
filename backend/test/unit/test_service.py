import pytest


@pytest.fixture(scope="function")
def get_exchange_rate():
    return {"Valute": {"USD": {"Value": 95.6}}}


def test_check_cache(get_exchange_rate):
    pass
