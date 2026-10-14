import pytest
import pytest_check as check

@pytest.fixture(scope='session')
def greetings():
    print("Before test step..")
    print("Hello!")
    yield
    print("after test step..")
    print("Bye !")