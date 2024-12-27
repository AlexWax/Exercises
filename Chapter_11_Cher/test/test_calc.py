import pytest
import unittest
import Study.Chapter_11_Cher.calcul.calc as c
Calc = c.Calc
from Study.Chapter_11_Cher.test.conftest import input_value

class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calc()

    def tearDown(self) -> None:
        ...

    def test_sum(self):
        self.assertEquals(self.calculator.sum(input_value, 2), 5)

    def test_sub(self):
        self.assertEquals(self.calculator.sub(input_value, 2), 5)


if __name__ == '__main__':
    unittest.main()