import pytest
from src.calculadora import (
    sumar, restar, multiplicar, dividir, 
    potencia, raiz_cuadrada, promedio
)

def test_sumar():
    # 1. Arrange
    a, b = 5, 3
    # 2. Act
    res = sumar(a, b)
    # 3. Assert
    assert res == 8

def test_restar():
    # 1. Arrange
    a, b = 10, 4
    # 2. Act
    res = restar(a, b)
    # 3. Assert
    assert res == 6

def test_multiplicar():
    # 1. Arrange
    a, b = 6, 7
    # 2. Act
    res = multiplicar(a, b)
    # 3. Assert
    assert res == 42

def test_dividir_exitoso():
    # 1. Arrange
    a, b = 20, 4
    # 2. Act
    res = dividir(a, b)
    # 3. Assert
    assert res == 5.0

def test_dividir_por_cero_lanza_excepcion():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_potencia():
    # 1. Arrange
    base, exp = 2, 3
    # 2. Act
    res = potencia(base, exp)
    # 3. Assert
    assert res == 8

def test_promedio_lista():
    # 1. Arrange
    numeros = [10, 20, 30]
    # 2. Act
    res = promedio(numeros)
    # 3. Assert
    assert res == 20.0