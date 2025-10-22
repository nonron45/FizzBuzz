from  fizzBuzz import fizzBuzz
import pytest
@pytest.mark.parametrize("n, expected_result",[(0,0),(1,1),(2,2)])

def test_fizzBuzz0return1 (n, expected_result):
    result:int  = fizzBuzz(n)
    assert  result == expected_result