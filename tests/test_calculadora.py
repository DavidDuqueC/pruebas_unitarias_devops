import pytest
from src.calculadora import (
    sumar, restar, multiplicar, dividir, 
    potencia, raiz_cuadrada, promedio, maximo, minimo
)

def test_sumar():
    # 1. Arrange + 2. Act + 3. Assert
    assert sumar(5, 3) == 8
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    # 1. Arrange + 2. Act + 3. Assert
    assert restar(10, 4) == 6
    assert restar(5, 10) == -5

def test_multiplicar():
    # 1. Arrange + 2. Act + 3. Assert
    assert multiplicar(6, 7) == 42
    assert multiplicar(-3, 5) == -15
    assert multiplicar(5, 0) == 0

def test_dividir_exitoso():
    # 1. Arrange + 2. Act + 3. Assert
    assert dividir(20, 4) == 5.0
    assert dividir(7, 2) == 3.5

def test_dividir_por_cero():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_potencia():
    # 1. Arrange + 2. Act + 3. Assert
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(2, -1) == 0.5

def test_raiz_cuadrada_exitosa():
    # 1. Arrange + 2. Act + 3. Assert
    assert raiz_cuadrada(9) == 3.0
    assert raiz_cuadrada(0) == 0.0

def test_raiz_cuadrada_negativa():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        raiz_cuadrada(-4)

def test_promedio_lista():
    # 1. Arrange + 2. Act + 3. Assert
    assert promedio([10, 20, 30]) == 20.0
    assert promedio([5]) == 5.0

def test_promedio_lista_vacia():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        promedio([])

def test_maximo_y_minimo():
    # 1. Arrange + 2. Act + 3. Assert
    numeros = [4, 2, 9, 1, 7]
    assert maximo(numeros) == 9
    assert minimo(numeros) == 1

def test_maximo_minimo_vacio():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        maximo([])
    with pytest.raises(ValueError):
        minimo([])