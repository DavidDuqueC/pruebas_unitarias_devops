import pytest
from src.utils import es_primo, mcd, es_bisiesto, categorizar_imc

def test_es_primo_numero_primo():
    # 1. Arrange
    numero = 7

    # 2. Act
    resultado = es_primo(numero)

    # 3. Assert
    assert resultado is True

def test_es_bisiesto_año_bisiesto():
    # 1. Arrange
    anio = 2024

    # 2. Act
    resultado = es_bisiesto(anio)

    # 3. Assert
    assert resultado is True

def test_mcd_numeros_enteros():
    # 1. Arrange
    a = 48
    b = 18
    esperado = 6

    # 2. Act
    resultado = mcd(a, b)

    # 3. Assert
    assert resultado == esperado

def test_categorizar_imc_normal():
    # 1. Arrange
    imc = 22.0
    esperado = "Normal"

    # 2. Act
    resultado = categorizar_imc(imc)

    # 3. Assert
    assert resultado == esperado