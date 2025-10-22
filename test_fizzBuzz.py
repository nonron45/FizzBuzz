import pytest
def fizzBuzz (n:int)-> int:
    if n==0:
          return 0
def test_fizzBuzz0return1 ():
    result = fizzBuzz(0)
    assert  result ==0