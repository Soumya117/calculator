from decimal import Decimal
from pydantic import BaseModel


class Calculator(BaseModel):
    """
    A simple class that performs some basic
    mathematical operations.
    The supported operations are:
    - Addition
    - Subtraction
    - Multiplication
    - Division
    """
    input_1: Decimal
    input_2: Decimal
    action: str

    def _add(self) -> Decimal:
        # add two numbers
        return self.input_1 + self.input_2

    def _subtract(self) -> Decimal:
        # subtracts two numbers
        return self.input_1 - self.input_2

    def _multiply(self) -> Decimal:
        # multiplies two numbers
        return self.input_1 * self.input_2

    def _divide(self) -> Decimal:
        # divides two numbers
        # raise DivisionByZero error
        return self.input_1 / self.input_2

    def perform(self) -> Decimal:
        """
        Perform the selected action
        """
        actions_dict: dict = {
            '1': self._add,
            '2': self._subtract,
            '3': self._multiply,
            '4': self._divide,
        }
        return actions_dict[self.action]()
