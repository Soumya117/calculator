# calculator interface to use the calculator class
from pydantic import ValidationError

from calculator import Calculator
from decimal import Decimal


class CalculatorInterface:
    """
    Interface method to create the calculator class
    and handle all the exceptions.
    This class should be called instead of the calculator
    class directly.
    """
    @staticmethod
    def perform(input_1: Decimal, input_2: Decimal, action: str) -> tuple[int | None, str]:
        error_str: str = 'Invalid operation: '
        try:
            calculator = Calculator(
                input_1=input_1,
                input_2=input_2,
                action=action
            )
            return calculator.perform(), ''
        except ZeroDivisionError:
            return None, error_str + 'Division by zero is raised'
        except KeyError:
            return None, f'{error_str} {action} is not supported'
        except ValidationError as e:
            return None, f'Action failed with validation error: {e}'