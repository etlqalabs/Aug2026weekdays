import pytest
from sqlalchemy import create_engine
import pandas as pd

'''
# Parameterized tests

@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.parametrize("a,b,expected",[(1,2,3),(4,5,10),(10,10,20)])
def test_compare(a,b,expected):
    assert a+b == expected

#Markers  : categorizing test cases, we can define custom markers like smoke, regresison, dq etc.
# pre defined markers by pytest  : skip,xfail

@pytest.mark.regression
def test_compare_2_numbers_test_1():
    assert 1 == 1,"Both numbers are not equals - test 1"


@pytest.mark.regression
@pytest.mark.skip
def test_compare_2_numbers_test_2():
    assert 1 == 1,"Both numbers are not equals - test 2"

@pytest.mark.smoke
@pytest.mark.xfail
def test_compare_2_numbers_test_3():
    assert 2 == 1,"Both numbers are not equals- test 3"


def test_count_check():
    df = pd.read_sql("select * from product",mysql_conn)
    count_actual = df.size
    print("actaul count :",count_actual)
    count_expected = 140
    assert count_expected == count_actual,"Row count not matching with expected.."

def test_count_check2():
    df = pd.read_sql("select * from product",mysql_conn)
    count_actual = df.size
    print("actaul count :",count_actual)
    count_expected = 140
    assert count_expected == count_actual,"Row count not matching with expected.."

def test_count_check3():
    df = pd.read_sql("select * from product",mysql_conn)
    count_actual = df.size
    print("actaul count :",count_actual)
    count_expected = 140
    assert count_expected == count_actual,"Row count not matching with expected.."


# use fixture
def test_count_check4(get_dataframe):
    count_actual = get_dataframe.size
    print("actaul count :",count_actual)
    count_expected = 140
    assert count_expected == count_actual,"Row count not matching with expected.."
'''

def test_compare_data_in_two_files(read_source_file,read_target_file):
    assert read_source_file.equals(read_target_file),("Both files have different data")

# Parallel runs demo
@pytest.mark.order(4)
def test_compare_data_in_two_files_1(read_source_file,read_target_file):

    #print(read_source_file)
    #print(read_target_file)
    assert read_source_file.equals(read_target_file),("Both files have different data")

@pytest.mark.order(3)
def test_compare_data_in_two_files_2(read_source_file,read_target_file):

    assert 1==2,"both are not same"

@pytest.mark.order(5)
@pytest.mark.regression
def test_compare_data_in_two_files_3(read_source_file,read_target_file):
    assert read_source_file.equals(read_target_file),("Both files have different data")

@pytest.mark.order(2)
@pytest.mark.smoke
def test_compare_data_in_two_files_4(read_source_file,read_target_file):
    assert read_source_file.equals(read_target_file),("Both files have different data")

@pytest.mark.order(1)
@pytest.mark.smoke
def test_compare_data_in_two_files_5(read_source_file,read_target_file):
    assert read_source_file.equals(read_target_file),("Both files have different data")

