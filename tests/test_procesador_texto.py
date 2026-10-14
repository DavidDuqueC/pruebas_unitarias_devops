import pytest
from src.procesador_texto import (
    contar_palabras, contar_vocales, invertir_texto, 
    es_palindromo, convertir_mayusculas, limpiar_texto
)

def test_contar_palabras():
    # 1. Arrange
    texto = "Hola mundo de DevOps"
    # 2. Act
    res = contar_palabras(texto)
    # 3. Assert
    assert res == 4

def test_contar_vocales():
    # 1. Arrange
    texto = "AEIOUaeiou"
    # 2. Act
    res = contar_vocales(texto)
    # 3. Assert
    assert res == 10

def test_invertir_texto():
    # 1. Arrange
    texto = "hola"
    # 2. Act
    res = invertir_texto(texto)
    # 3. Assert
    assert res == "aloh"

def test_es_palindromo():
    # 1. Arrange
    texto = "reconocer"
    # 2. Act
    res = es_palindromo(texto)
    # 3. Assert
    assert res is True

def test_convertir_mayusculas():
    # 1. Arrange
    texto = "prueba"
    # 2. Act
    res = convertir_mayusculas(texto)
    # 3. Assert
    assert res == "PRUEBA"

def test_limpiar_texto():
    # 1. Arrange
    texto = "Hola_Mundo! 123."
    # 2. Act
    res = limpiar_texto(texto)
    # 3. Assert
    assert res == "HolaMundo 123"