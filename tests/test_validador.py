import pytest
from src.validador import (
    validar_email,
    validar_telefono,
    validar_edad,
    validar_password,
    validar_url,
    validar_fecha,
    validar_cedula
)

def test_validar_email_exitoso():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_email("usuario@example.com") is True

def test_validar_email_invalidos():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_email("") is False
    assert validar_email("usuarionosignodepunto") is False
    assert validar_email("@example.com") is False
    assert validar_email("usuario@.com") is False
    assert validar_email("usuario@dominio@com") is False

def test_validar_telefono():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_telefono("3001234567") is True
    assert validar_telefono("300 123-4567") is True
    assert validar_telefono("123456") is False  # Muy corto
    assert validar_telefono("1234567890123456") is False  # Muy largo
    assert validar_telefono("abc-123456") is False
    assert validar_telefono("") is False

def test_validar_edad():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_edad(25) is True
    assert validar_edad(0) is True
    assert validar_edad(120) is True
    assert validar_edad(-1) is False
    assert validar_edad(121) is False
    assert validar_edad("veinticinco") is False

def test_validar_password():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_password("SecurePass1") is True
    assert validar_password("short1A") is False      # Menos de 8 caracteres
    assert validar_password("alllowercase1") is False  # Sin mayúscula
    assert validar_password("ALLUPPERCASE1") is False  # Sin minúscula
    assert validar_password("NoNumbersHere") is False  # Sin números
    assert validar_password("") is False

def test_validar_url():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_url("https://www.google.com") is True
    assert validar_url("http://example.com/path?query=1") is True
    assert validar_url("ftp://example.com") is False
    assert validar_url("www.google.com") is False
    assert validar_url("") is False

def test_validar_fecha_valida_y_bug():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_fecha(15, 6, 2026) is True
    # BUG expuesto: El código actual acepta el 31 de febrero porque solo valida que el día esté entre 1 y 31
    # Esto debería retornar False, pero el código erróneo retorna True.
    assert validar_fecha(31, 2, 2026) is False

def test_validar_fecha_invalidas():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_fecha(32, 5, 2026) is False
    assert validar_fecha(15, 13, 2026) is False
    assert validar_fecha(15, 5, 1800) is False
    assert validar_fecha("15", 5, 2026) is False

def test_validar_cedula():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_cedula(12345678) is True
    assert validar_cedula("1234567890") is True
    assert validar_cedula(12345) is False     # Menos de 6 dígitos
    assert validar_cedula(12345678901) is False # Más de 10 dígitos
    assert validar_cedula("abc12345") is False
    assert validar_cedula("") is False