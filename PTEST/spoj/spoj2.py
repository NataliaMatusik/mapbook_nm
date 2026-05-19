from PTEST.adder import adders

t = int(input('Wprowadz liczbe testow:'))
for i in range(t):
    n= int(input('Wprowadz ilosc liczb:'))
    # print(n)
    lista_liczb=list(map(int, input().split()))
    print(sum(lista_liczb))


# reader 
from typing import Protocol, List 

class DataInput(Protocol):
    def read_digit(self)-> int: ...
    def read_line_of_digits(self)-> List[str]: ...
    
class TerminalInput:
    def read_digit(self)-> int:
        return int(input())
    
    def read_line_of_digits(self)-> List[str]:
        return input().split()
    



# busieness logic
class DataTransform:
    def transform_data(self, list_of_stings) -> List[int]:...


class TerminalTransform:
    def list_transform(self,list_of_strings) -> List[int]:
        return list(map(int, list_of_strings))
    
class DataAdder(Protocol):
    def add_data(self, digits:List[int]) -> int:...
        
class TerminalAdder:
    def add_data(self, digits: List[int]) -> int:
        return sum(digits)
        
# output
class ResultWriter(Protocol):
    def write_results(self, results: int) -> None: 
        print(results)

# services
class RNO_DODService:
    def __init__(
            self, 
            reader: DataInput, 
            writer: ResultWriter, 
            transformer: DataTransform, 
            add:adders,
            adder: DataAdder):
        self.reader = reader
        self.writer = writer
        self.transformer = transformer
        self.add = add
        self.adder = adder
    def execute(self, list_of_digits=None):
        t=self.reader.read_digit()
        line_of_strings=self.reader.read_line_of_digits()
        list_of_strings=self.transformer.list_transform(line_of_strings)
        result=self.adder.add_data(list_of_digits)
        self.writer.write_results(result)
        
class RMO_DODApp:
    @staticmethod
    def run():
        reader = TerminalInput()
        writer = ResultWriter()
        transformer = TerminalTransform()
        adder = TerminalAdder()
        
        service = RNO_DODService(reader, writer, transformer, adder)
        service.execute()
        
        service=RNO_DODService(reader, writer, transformer, adder)
        service.execute()
        
if __name__ == '__main__':
    RNO_DODService().run()
    
        
        
# app