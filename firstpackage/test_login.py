import pytest


@pytest.fixture()
def setup_and_teardown():
    print("open Browser")
    print("Enter Url")
    yield
    print("Close Browser")

@pytest.mark.smoke
def test_login_with_valid_credentails(setup_and_teardown):
    print("login with valid credentials")

@pytest.mark.regression
def test_login_with_invalid_credentials(setup_and_teardown):
    print("login with invalid credentials")