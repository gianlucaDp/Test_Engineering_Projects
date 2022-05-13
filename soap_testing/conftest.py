import pytest

from soap_testing.objects.CalculatorClient import CalculatorClient


@pytest.fixture
def calculator():
    return CalculatorClient()
