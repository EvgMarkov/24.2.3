import pytest

from app.calc import Calculator

class TestClass:
    def setup(self):
        self.calc = Calculator

    def test_sum_success(self):
        assert self.calc.adding(self, 2, 3) == 5

    def test_mult_success(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_div_success(self):
         assert self.calc.division(self, 6, 2) == 3

    def test_sub_success(self):
         assert self.calc.substraction(self, 5, 2) == 3

    def teardown(self):
        print("Выполнение метода Teardown")



