import pytest
from src.conversor import (
    celsius_a_fahrenheit,
    metros_a_kilometros,
    libras_a_kilogramos,
    kilogramos_a_libras
)

def test_celsius_a_fahrenheit():
    # 1. Arrange (Preparar)
    celsius = 25
    esperado = 77.0

    # 2. Act (Actuar)
    resultado = celsius_a_fahrenheit(celsius)

    # 3. Assert (Afirmar)
    assert resultado == esperado

def test_metros_a_kilometros():
    # 1. Arrange (Preparar)
    metros = 1500
    esperado = 1.5

    # 2. Act (Actuar)
    resultado = metros_a_kilometros(metros)

    # 3. Assert (Afirmar)
    assert resultado == esperado

def test_libras_a_kilogramos():
    # 1. Arrange (Preparar)
    libras = 10
    esperado = 4.53592

    # 2. Act (Actuar)
    resultado = libras_a_kilogramos(libras)

    # 3. Assert (Afirmar)
    assert resultado == esperado

def test_distancia_negativa():
    # 1. Arrange (Preparar)
    metros_negativos = -500

    # 2. Act + 3. Assert 
    with pytest.raises(ValueError, match="La distancia no puede ser negativa"):
        metros_a_kilometros(metros_negativos)