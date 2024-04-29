import pytest


@pytest.fixture()
def setup_and_teardown():
    print("Login using valid cedentials")
    yield
    print("Close system")


@pytest.mark.smoke
def test_login1_with_valid_credentials(setup_and_teardown):
    print("Login into the website")


@pytest.mark.regression
def test_login1_with_invalid_credentials(setup_and_teardown):
    print("Login unsuccessful")