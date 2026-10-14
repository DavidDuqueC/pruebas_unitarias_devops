import pytest
from src.calculadora import sumar, dividir, promedio

def test_sumar_positivos():
    # 1. Arrange (Preparar)
    a = 5
    b = 3
    resultado_esperado = 8

    # 2. Act (Actuar)
    resultado_obtenido = sumar(a, b)

    # 3. Assert (Afirmar)
    assert resultado_obtenido == resultado_esperado

def test_dividir():
    # 1. Arrange (Preparar)
    a = 10
    b = 5
    resultado_esperado = 2.0

    # 2. Act (Actuar)
    resultado_obtenido = dividir(a, b)

    # 3. Assert (Afirmar)
    assert resultado_obtenido == resultado_esperado
  

def test_promedio_lista():
    # 1. Arrange (Preparar)
    numeros = [2, 4, 6, 8]
    resultado_esperado = 5.0

    # 2. Act (Actuar)
    resultado_obtenido = promedio(numeros)

    # 3. Assert (Afirmar)
    assert resultado_obtenido == resultado_esperado