import pytest
from src.fibonacci import (
    fibonacci_iterativo, 
    fibonacci_recursivo, 
    fibonacci_serie, 
    es_fibonacci
)

def test_fibonacci_iterativo_casos_base():
    # 1. Arrange + 2. Act + 3. Assert
    assert fibonacci_iterativo(0) == 0
    assert fibonacci_iterativo(1) == 1

def test_fibonacci_iterativo_secuencia():
    # 1. Arrange + 2. Act + 3. Assert
    assert fibonacci_iterativo(5) == 5
    assert fibonacci_iterativo(6) == 8
    assert fibonacci_iterativo(10) == 55

def test_fibonacci_iterativo_negativo_lanza_error():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        fibonacci_iterativo(-1)

def test_fibonacci_recursivo_casos_base():
    # 1. Arrange + 2. Act + 3. Assert
    assert fibonacci_recursivo(0) == 0
    assert fibonacci_recursivo(1) == 1

def test_fibonacci_recursivo_secuencia():
    # 1. Arrange + 2. Act + 3. Assert
    assert fibonacci_recursivo(4) == 3
    assert fibonacci_recursivo(7) == 13

def test_fibonacci_recursivo_negativo_lanza_error():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        fibonacci_recursivo(-3)

def test_fibonacci_serie_valida():
    # 1. Arrange + 2. Act + 3. Assert
    assert fibonacci_serie(0) == [0]
    assert fibonacci_serie(1) == [0, 1]
    assert fibonacci_serie(5) == [0, 1, 1, 2, 3, 5]

def test_fibonacci_serie_negativa_lanza_error():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        fibonacci_serie(-2)

def test_es_fibonacci_verdadero():
    # 1. Arrange + 2. Act + 3. Assert
    assert es_fibonacci(0) is True
    assert es_fibonacci(1) is True
    assert es_fibonacci(8) is True
    assert es_fibonacci(21) is True

def test_es_fibonacci_falso():
    # 1. Arrange + 2. Act + 3. Assert
    assert es_fibonacci(4) is False
    assert es_fibonacci(10) is False
    assert es_fibonacci(-1) is False