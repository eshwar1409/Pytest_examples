import pytest


class TestMathOperations:
    def test_addition(T1):
        assert 1 + 2 == 3

    def test_subtraction(T2):
        assert 4 - 2 == 2


    def test_multiplication(T3):
        assert 3 * 4 == 12

    def test_division(T4):
        assert 8 / 2 == 4

if __name__ == "__main__":
  pytest.main()




