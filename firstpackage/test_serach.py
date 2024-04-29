import pytest


@pytest.fixture()
def setup_and_teardown():
    print("Search product")
    yield
    print("Do not search")


@pytest.mark.smoke
def test_search_valid_product(setup_and_teardown):
    print("Search valid product")


@pytest.mark.regression
def test_search_invalid_product(setup_and_teardown):
    print("Search invalid product")