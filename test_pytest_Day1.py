import pytest
import pytest_check as check

'''
def test_compare_2_numbers_test_1():
    assert 1 == 1,"Both numbers are not equals - test 1"


def test_compare_2_numbers_test_2():
    assert 1 == 1,"Both numbers are not equals - test 2"

def test_compare_2_numbers_test_3():
    assert 2 == 1,"Both numbers are not equals- test 3"


# Assertion
# Hard assertion
def test_compare_2_numbers_test_HardAssert():
    assert 1 == 1,"Both numbers are not equals - test 1"
    assert 1 == 2, "Both numbers are equals - test 2"
    assert 2 == 3, "Both numbers are not equals - test 3"
    assert 3 == 3, "Both numbers are equals - test 4"
    assert 5 == 3, "Both numbers are equals - test 5"

# Soft assertion
def test_compare_2_numbers_test_softAssert():
    check.equal(1,1,"Both numbers are not equals - test 1")
    check.equal(1,2,"Both numbers are equals - test 2")
    check.is_true(2==3,"Both numbers are not equals - test 3")
    check.is_true(3 == 3, "Both numbers are equals - test 4")
    check.is_true(5 == 3, "Both numbers are equals - test 5")


# Fixtures without fixture
def test_welcome_message_1():
    print("Hello !")
    print("Welcome Mr. ABC !")
    print("Bye !")

def test_welcome_message_2():
    print("Hello !")
    print("Welcome Mr. XYZ !")
    print("Bye !")



# write a fixture at function or at every test case level
@pytest.fixture(scope='function')
def greetings():
    print("Before test step..")
    print("Hello!")
    yield
    print("after test step..")
    print("Bye !")

def test_welcome_message_1(greetings):
    print("Welcome Mr. ABC !")

def test_welcome_message_2(greetings):
    print("Welcome Mr. XYZ !")



# write a fixture at module or file level
@pytest.fixture(scope='module')
def greetings():
    print("Before test step..")
    print("Hello!")
    yield
    print("after test step..")
    print("Bye !")

def test_welcome_message_1(greetings):
    print("Welcome Mr. ABC !")

def test_welcome_message_2(greetings):
    print("Welcome Mr. XYZ !")

def test_welcome_message_3(greetings):
    print("Welcome Mr. Last !")

'''

# write a fixture at module or file level

def test_welcome_message_1(greetings):
    print("Welcome Mr. ABC !")

def test_welcome_message_2(greetings):
    print("Welcome Mr. XYZ !")

def test_welcome_message_3(greetings):
    print("Welcome Mr. Last !")



