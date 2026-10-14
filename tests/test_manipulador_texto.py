import pytest
from src.manipulador_texto import (
    invertir_cadena, contar_consonantes, eliminar_duplicados, 
    extraer_dominio, enmascarar_email, es_anagrama
)

def test_invertir_cadena():
    # 1. Arrange
    cadena = "devops"
    # 2. Act
    res = invertir_cadena(cadena)
    # 3. Assert
    assert res == "spoved"

def test_contar_consonantes():
    # 1. Arrange
    cadena = "bcd"
    # 2. Act
    res = contar_consonantes(cadena)
    # 3. Assert
    assert res == 3

def test_eliminar_duplicados():
    # 1. Arrange
    cadena = "aabbcc"
    # 2. Act
    res = eliminar_duplicados(cadena)
    # 3. Assert
    assert res == "abc"

def test_extraer_dominio():
    # 1. Arrange
    email = "usuario@example.com"
    # 2. Act
    res = extraer_dominio(email)
    # 3. Assert
    assert res == "example.com"

def test_enmascarar_email():
    # 1. Arrange
    email = "test@example.com"
    # 2. Act
    res = enmascarar_email(email)
    # 3. Assert
    assert res == "t**t@example.com"

def test_es_anagrama():
    # 1. Arrange
    c1, c2 = "roma", "amor"
    # 2. Act
    res = es_anagrama(c1, c2)
    # 3. Assert
    assert res is True