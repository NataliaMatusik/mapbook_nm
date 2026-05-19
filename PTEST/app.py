# zmienna_A=int(input())
# zmienna_B=int(input())
#
# print(zmienna_A+zmienna_B)

from typing import Protocol, List
from reader.input_readers import DataInput, TerminalInput
from writer.output_writer import ResultWriter
from adder.adders import DataAdder, Adder

# READER
class DataInput(Protocol):
    def read_data(self) -> int:
        ...


class TerminalInput:
    def read_data(self) -> int:
        return int(input())


# WRITER
class ResultWriter(Protocol):
    def write_data(self, value) -> None:
        ...


class TerminalWriter:
    def write_data(self, value) -> None:
        print(value)

class FileWriter:
    def write_data(self, value) -> None:
        with open('result.txt', 'a') as f:
            f.write(f'{value}')


# BUSINESS LOGIC
class DataAdder(Protocol):
    def add_data(self, Digit_A: int, Digit_B: int) -> int:
        ...


class Adder:
    def add_data(self, Digit_A: int, Digit_B: int) -> int:
        return Digit_A + Digit_B


# SERVICE
class PTESTService:
    def __init__(self, reader: DataInput, writer: ResultWriter, adder: DataAdder):
        self.reader = reader
        self.writer = writer
        self.adder = adder

    def execute(self):
        digit_A = self.reader.read_data()
        digit_B = self.reader.read_data()
        result = self.adder.add_data(digit_A, digit_B)
        self.writer.write_data(result)


# APP
class PTESTApp:
    @staticmethod
    def run():
        reader = TerminalInput()
        writer = FileWriter()
        adder = Adder()

        service = PTESTService(reader, writer, adder)
        service.execute()


if __name__ == '__main__':
    PTESTApp.run()    