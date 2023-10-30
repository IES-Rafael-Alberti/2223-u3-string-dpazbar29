import pytest 
from src.E_3_0_4 import *

@pytest.mark.parametrize(
    "input_x,input_y,input_z,input_r,expected",
    [
        ("banana","a","n","b",[3,2,1])
    ]
)

def test_contarLetras(input_x,input_y,input_z,input_r,expected):
    assert contarLetras(input_x,input_y,input_z,input_r) == expected


@pytest.mark.parametrize(
    "input_x,input_y,input_z,input_r,expected",
    [
        ("a","n","b",[3,2,1],"La letra a aparece: 3 veces\nLa letra n aparece: 2 veces\nLa letra b aparece: 1 vez")
    ]
)

def test_mensajeSalida(input_x,input_y,input_z,input_r,expected):
    assert MensajeSalida(input_x,input_y,input_z,input_r) == expected