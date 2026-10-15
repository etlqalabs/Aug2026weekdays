import pytest
import pytest_check as check
from sqlalchemy import create_engine
import pandas as pd

mysql_conn = create_engine("mysql+pymysql://root:Admin%40143@localhost:3308/aug_2026")


@pytest.fixture(scope='session')
def greetings():
    print("Before test step..")
    print("Hello!")
    yield
    print("after test step..")
    print("Bye !")

# Autouse
@pytest.fixture(scope='function',autouse=True)
def message():
    print("test started.....")
    yield
    print("test completed.....")

# Define fixtire to get a dataframe

@pytest.fixture(scope='session')
def get_dataframe():
    df = pd.read_sql("select * from product", mysql_conn)
    yield df
    print("closing db conneciton")

@pytest.fixture()
def read_source_file():
    df_emp_src = pd.read_csv("emp.csv")
    yield df_emp_src

@pytest.fixture()
def read_target_file():
    df_employees_tgt = pd.read_csv("employees.csv")
    yield df_employees_tgt

# Parallel runs