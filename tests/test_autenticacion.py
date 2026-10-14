import pytest
from src.autenticacion import (
    hash_contraseña, verificar_contraseña, 
    validar_usuario, generar_token, validar_token,
    generar_codigo_2fa, verificar_codigo_2fa, sanear_entrada
)

def test_validar_usuario_limite_minimo():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_usuario("abc") is True
    assert validar_usuario("ab") is False

def test_validar_usuario_limite_maximo():
    # 1. Arrange + 2. Act + 3. Assert
    usuario_valido = "a" * 20
    usuario_largo = "a" * 21
    assert validar_usuario(usuario_valido) is True
    assert validar_usuario(usuario_largo) is False

def test_validar_usuario_caracteres_especiales():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_usuario("user.name") is False
    assert validar_usuario("user-name") is False
    assert validar_usuario("user name") is False
    assert validar_usuario("user@123") is False

def test_validar_usuario_nulo_o_vacio():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_usuario("") is False
    assert validar_usuario(None) is False

def test_hash_contraseña_vacia_o_atipica():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises((AttributeError, TypeError)):
        hash_contraseña(None)

def test_verificar_contraseña_incorrecta():
    # 1. Arrange + 2. Act + 3. Assert
    pwd = "PasswordSeguro123"
    h = hash_contraseña(pwd)
    assert verificar_contraseña("PasswordFalso123", h) is False

def test_validar_token_casos_atipicos():
    # 1. Arrange + 2. Act + 3. Assert
    assert validar_token("") is False
    assert validar_token(None) is False
    assert validar_token("abc123") is False  # Muy corto (< 32 chars)
    assert validar_token("g" * 32) is False  
    assert validar_token("z" * 32) is False  # 'z' no es un carácter hexadecimal válido

def test_verificar_codigo_2fa_atipico():
    # 1. Arrange + 2. Act + 3. Assert
    assert verificar_codigo_2fa("", "123456") is False
    assert verificar_codigo_2fa(None, "123456") is False
    assert verificar_codigo_2fa("123456", None) is False
    assert verificar_codigo_2fa("123456", "654321") is False

def test_sanear_entrada_atipica():
    # 1. Arrange + 2. Act + 3. Assert
    assert sanear_entrada("") == ""
    assert sanear_entrada(None) == ""
    entrada_maliciosa = "SELECT * FROM usuarios; -- 'OR' 1=1 <script>"
    saneada = sanear_entrada(entrada_maliciosa)
    assert ";" not in saneada
    assert "--" not in saneada
    assert "'" not in saneada
    assert "<" not in saneada
    assert ">" not in saneada