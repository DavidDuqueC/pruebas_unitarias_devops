import pytest
from src.manipulador_texto import (
    invertir_cadena,
    contar_vocales,
    contar_consonantes,
    es_palindromo,
    eliminar_duplicados,
    capitalizar_palabras,
    convertir_a_titulo,
    reemplazar_subcadena,
    dividir_en_palabras,
    extraer_dominio,
    enmascarar_email,
    normalizar_espacios,
    truncar,
    es_anagrama
)

def test_invertir_cadena():
    # 1. Arrange + 2. Act + 3. Assert
    assert invertir_cadena("hola") == "aloh"
    assert invertir_cadena("") == ""

def test_contar_vocales_y_consonantes():
    # 1. Arrange + 2. Act + 3. Assert
    assert contar_vocales("Hola Mundo") == 4
    assert contar_vocales("") == 0
    assert contar_consonantes("Hola Mundo") == 5
    assert contar_consonantes("") == 0

def test_es_palindromo_con_bug():
    # 1. Arrange + 2. Act + 3. Assert
    assert es_palindromo("radar") is True
    # BUG 1 expuesto: "Anita lava la tina" con espacios y mayúsculas fallará debido al bug actual
    assert es_palindromo("Anita lava la tina") is True
    assert es_palindromo("") is False

def test_eliminar_duplicados():
    # 1. Arrange + 2. Act + 3. Assert
    assert eliminar_duplicados("programacion") == "progamin"
    assert eliminar_duplicados("") == ""

def test_capitalizar_y_titulo():
    # 1. Arrange + 2. Act + 3. Assert
    assert capitalizar_palabras("hola mundo devops") == "Hola Mundo Devops"
    assert capitalizar_palabras("") == ""
    assert convertir_a_titulo("hola mundo") == "Hola Mundo"
    assert convertir_a_titulo("") == ""

def test_reemplazar_subcadena():
    # 1. Arrange + 2. Act + 3. Assert
    assert reemplazar_subcadena("hola mundo", "mundo", "devops") == "hola devops"
    assert reemplazar_subcadena("", "a", "b") == ""

def test_dividir_en_palabras_con_bug():
    # 1. Arrange + 2. Act + 3. Assert
    assert dividir_en_palabras("uno dos tres") == ["uno", "dos", "tres"]
    # BUG 2 expuesto: Múltiples espacios seguidos romperán el split(' ') simple
    assert dividir_en_palabras("uno  dos") == ["uno", "dos"]

def test_correos_manipulacion():
    # 1. Arrange + 2. Act + 3. Assert
    assert extraer_dominio("usuario@example.com") == "example.com"
    assert extraer_dominio("invalido") == ""
    assert enmascarar_email("david@example.com") == "d***d@example.com"
    assert enmascarar_email("io@example.com") == "io@example.com"
    assert enmascarar_email("invalido") == ""

def test_normalizar_espacios_y_truncar():
    # 1. Arrange + 2. Act + 3. Assert
    assert normalizar_espacios("hola    mundo   devops") == "hola mundo devops"
    assert normalizar_espacios("") == ""
    assert truncar("Hola mundo", 8, "...") == "Hola..."
    assert truncar("Hi", 10, "...") == "Hi"
    assert truncar("", 5) == ""

def test_es_anagrama():
    # 1. Arrange + 2. Act + 3. Assert
    assert es_anagrama("listen", "silent") is True
    assert es_anagrama("hello", "world") is False
    assert es_anagrama("", "test") is False