from  fizzBuzz import fizzBuzz
import pytest
@pytest.mark.parametrize("n, expected_result",[(0,'0'),(1,'1'),(2,'2'),(3,"Fizz")])

def test_fizzBuzz0return1 (n:int, expected_result: str):
    result:int  = fizzBuzz(n)
    assert  result == expected_result