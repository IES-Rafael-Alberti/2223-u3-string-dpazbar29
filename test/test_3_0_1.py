import pytest 
from src.E_3_0_1 import *

@pytest.mark.parametrize(
    "input_x,expected",
    [
        ("hola","a\nl\no\nh")
    ]
)

def test_obtenerCadena(input_x,expected):
    assert obtenerCadena(input_x) == expected