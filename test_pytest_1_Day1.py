import pytest
import pytest_check as check
# write a fixture at module or file level

def test_welcome_message_3(greetings):
    print("Welcome Mr. abc !")

def test_welcome_message_5(greetings):
    print("Welcome Mr. xyz !")

def test_welcome_message_6(greetings):
    print("Welcome Mr. final !")




