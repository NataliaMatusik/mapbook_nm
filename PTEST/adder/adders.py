from typing import Protocol
# BUSINESS LOGIC
class DataAdder(Protocol):
    def add_data(self, Digit_A: int, Digit_B: int) -> int:
        ...


class Adder:
    def add_data(self, Digit_A: int, Digit_B: int) -> int:
        return Digit_A + Digit_B