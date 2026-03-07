import pytest

@pytest.fixture(scope="module")
def test_initialCheck():
    print("Hello this is the initial check test case")
    return "Initial Check Completed"
@pytest.mark.smoke
def test_case1(test_initialCheck):
    print("This is the test case 1")
    assert test_initialCheck == "Initial Check Completed"

@pytest.mark.smoke
def test_case2(pre_initialCheck):
    print("This is the test case 2")