import pytest


@pytest.fixture()
def setup_and_teardown():
    print("Open Data")
    yield
    print("Collect Data")

@pytest.mark.smoke
def test_collect_package(setup_and_teardown):
    print("Total package collected")


@pytest.mark.regression
def test_collect_wrong_package(setup_and_teardown):
    print("Collected wrong package")


@pytest.mark.parametrize("f_name,l_name",[("Adi","kumar"),("Aditya","kumar"),("Sunny","raj")])
def test_update_name(f_name,l_name,setup_and_teardown):
    print(f_name+" "+l_name)


