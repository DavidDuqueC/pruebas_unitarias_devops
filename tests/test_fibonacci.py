import pytest
from src.fibonacci import fibonacci_iterativo, fibonacci_serie, es_fibonacci

def test_fibonacci_iterativo_cero():
    # 1. Arrange
    n = 0
    esperado = 0

    # 2. Act
    resultado = fibonacci_iterativo(n)

    # 3. Assert
    assert resultado == esperado

def test_fibonacci_iterativo_positivo():
    # 1. Arrange
    n = 6
    esperado = 8  

    # 2. Act
    resultado = fibonacci_iterativo(n)

    # 3. Assert
    assert resultado == esperado

def test_fibonacci_negativo_lanza_error():
    # 1. Arrange & 2. Act & 3. Assert
    with pytest.raises(ValueError):
        fibonacci_iterativo(-1)

def test_es_fibonacci_valido():
    # 1. Arrange
    numero = 8

    # 2. Act
    resultado = es_fibonacci(numero)

    # 3. Assert
    assert resultado is True