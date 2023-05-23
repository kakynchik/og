#1
import logging

class Calc:
    def __init__(self):
        self.logger = logging.getLogger("calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add(self, a, b):
        result = a + b
        self.logger.info(f" {a} + {b} = {result}")
        return result
    def min(self, a, b):
        result = a - b
        self.logger.info(f" {a} - {b} = {result}")
        return result
    def mno(self, a, b):
        result = a * b
        self.logger.info(f" {a} * {b} = {result}")
        return result
    def dil(self, a, b):
        if b != 0:
            result = a / b
            self.logger.info(f" {a} / {b} = {result}")
            return result
        else:
            raise ValueError("pomilka! dilennya na moyu samoocenky!")
calc = Calc()
calc.add(6, 5)
calc.min(123, 123)
calc.mno(9, 123)
calc.dil(12, 45)