import pytest
from src.validador import validar_email, validar_telefono, validar_edad, validar_password

def test_validar_email_correcto():
    # 1. Arrange
    email = "usuario@ejemplo.com"

    # 2. Act
    resultado = validar_email(email)

    # 3. Assert
    assert resultado is True

def test_validar_email_no_arroba():
    # 1. Arrange
    email = "usuarioejemplo.com"

    # 2. Act
    resultado = validar_email(email)

    # 3. Assert
    assert resultado is False

def test_validar_telefono_valido():
    # 1. Arrange
    telefono = "3001234567"

    # 2. Act
    resultado = validar_telefono(telefono)

    # 3. Assert
    assert resultado is True

def test_validar_password_segura():
    # 1. Arrange
    password = "ClaveSegura123"

    # 2. Act
    resultado = validar_password(password)

    # 3. Assert
    assert resultado is True