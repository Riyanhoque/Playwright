import pytest



@pytest.fixture(scope="session")
def pre_initialCheck():
    print("This is the initial check test case")