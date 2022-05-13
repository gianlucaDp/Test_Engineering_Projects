from suds.cache import ObjectCache
from suds.client import Client


class CalculatorClient:
    def __init__(self):
        self.cache = ObjectCache()
        self.cache.location = "cache"
        self.cache.duration = 1
        self.client = Client(r"http://www.dneonline.com/calculator.asmx?wsdl", cache=self.cache)

    def add(self, a: int, b: int) -> int:
        return self.client.service.Add(a, b)

    def subtract(self, a: int, b: int) -> int:
        return self.client.service.Subtract(a, b)

    def divide(self, a: int, b: int) -> int:
        return self.client.service.Divide(a, b)

    def multiply(self, a: int, b: int) -> int:
        return self.client.service.Multiply(a, b)

