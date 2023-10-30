import pytest 
from src.E_3_0_3 import *

@pytest.mark.parametrize(
    "input_x,input_y,expected",
    [
        ("hola",1)
    ]
)

def test_cuenta(input_x,input_y,expected):
    assert cuenta(input_x,input_y) == expected