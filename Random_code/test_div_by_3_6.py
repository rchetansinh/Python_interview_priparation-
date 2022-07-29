import pytest
#@pytest.fixture
#def input_num():
#    input = 30
#    return input

def test_dev_by_3(input):
    print("3:",input)
    assert input % 3 == 0 

def test_dev_by_6(input):
    assert input  % 6 == 0 


'''
import pytest

@pytest.fixture
def input_value():
    input = 39
    return input

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0
'''
