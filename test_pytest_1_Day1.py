import pytest
import pytest_check as check
# write a fixture at module or file level

@pytest.mark.smoke
def test_welcome_message_3(greetings):
    print("Welcome Mr. abc !")

@pytest.mark.smoke
def test_welcome_message_5(greetings):
    print("Welcome Mr. xyz !")

@pytest.mark.smoke
def test_welcome_message_6(greetings):
    print("Welcome Mr. final !")




