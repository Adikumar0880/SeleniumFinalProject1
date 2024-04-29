import pytest


@pytest.fixture()
def setup_and_teardown():
    print("Register successfully")
    yield
    print("Registration got canceled")

@pytest.mark.smoke
def test_register_with_valid_credentials(setup_and_teardown):
    print("Register with valid credentials")

@pytest.mark.regression
def test_register_with_invalid_credentials(setup_and_teardown):
    print("Register with invalid credentials")