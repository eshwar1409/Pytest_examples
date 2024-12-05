import pytest


class TestMathOperations:
    def test_addition(self):
        assert 1 + 2 == 3

    def test_subtraction(self):
        assert 4 - 2 == 2


    def test_multiplication(self):
        assert 3 * 4 == 12

    def test_division(self):
        assert 8 / 2 == 2

if __name__ == "__main__":
  pytest.main()




