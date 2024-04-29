import pytest


@pytest.fixture()
def setup_and_teardown():
    print("Start doing registration process")
    yield
    print("Registration got cancelled")


@pytest.mark.smoke
def test_register1_with_valid_credentials(setup_and_teardown):
    print("Click on register link")


@pytest.mark.regression
def test_register1_with_invalid_credentials(setup_and_teardown):
    print("Registration unsuccessful")