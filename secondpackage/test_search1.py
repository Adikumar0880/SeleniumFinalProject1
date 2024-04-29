import pytest


@pytest.fixture()
def setup_and_teardown():
    print("Start searching")
    yield
    print("Product is not here")


@pytest.mark.smoke
def test_search_valid_product(setup_and_teardown):
    print("Product found")


@pytest.mark.xfail
# @pytest.mark.skip
@pytest.mark.smoke
@pytest.mark.regression
def test_search_invalid_product(setup_and_teardown):
    a = "Aditya"
    b = "Kumar"
    assert a==b,"a is not equal to b"