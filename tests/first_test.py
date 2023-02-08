import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 6, 4) == 24

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 81, 9) == 9

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 35, 6) == 29

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 41, 33) == 74
