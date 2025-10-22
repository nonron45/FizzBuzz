from  fizzBuzz import fizzBuzz
import pytest
@pytest.mark.parametrize("n, expected_result",[(0,'FizzBuzz'),(1,'1'),(2,'2'),(3,"Fizz"),(4,'4'),(5,"Buzz"),(6,"Fizz"),(7,'7')])

def test_fizzBuzz0return1 (n:int, expected_result: str):
    result:int  = fizzBuzz(n)
    assert  result == expected_result