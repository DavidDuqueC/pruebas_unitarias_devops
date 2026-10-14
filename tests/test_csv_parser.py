import pytest
from src.csv_parser import (
    parse_csv_line,
    leer_csv_como_lista,
    csv_a_diccionarios,
    validar_csv,
    extraer_columna,
    filtrar_por_columna,
    contar_filas,
    contar_columnas
)

def test_parse_csv_line():
    # 1. Arrange + 2. Act + 3. Assert
    assert parse_csv_line("a,b,c") == ["a", "b", "c"]
    assert parse_csv_line("") == []

def test_leer_csv_como_lista():
    # 1. Arrange
    csv_data = "nombre,edad\nAna,25"
    # 2. Act & 3. Assert
    assert leer_csv_como_lista(csv_data) == [["nombre", "edad"], ["Ana", "25"]]
    assert leer_csv_como_lista("") == []

def test_csv_a_diccionarios():
    # 1. Arrange
    csv_data = "nombre,edad\nAna,25"
    # 2. Act
    resultado = csv_a_diccionarios(csv_data, tiene_cabecera=True)
    # 3. Assert
    assert resultado == [{"nombre": "Ana", "edad": "25"}]
    assert csv_a_diccionarios("", tiene_cabecera=True) == []

def test_validar_csv():
    # 1. Arrange
    csv_valido = "a,b,c\n1,2,3"
    csv_invalido = "a,b,c\n1,2"
    # 2. Act & 3. Assert
    assert validar_csv(csv_valido) is True
    assert validar_csv(csv_invalido) is False
    assert validar_csv("") is False

def test_extraer_y_filtrar_columna():
    # 1. Arrange
    csv_data = "ciudad,activo\nBogota,true\nMedellin,false"
    # 2. Act & 3. Assert
    assert extraer_columna(csv_data, 0) == ["ciudad", "Bogota", "Medellin"]
    assert len(filtrar_por_columna(csv_data, 0, "Bogota")) == 2  # Incluye cabecera si coincide o según filas

def test_contar_filas_y_columnas():
    # 1. Arrange
    csv_data = "a,b,c\n1,2,3\n4,5,6"
    # 2. Act & 3. Assert
    assert contar_filas(csv_data) == 3
    assert contar_columnas(csv_data) == 3
    assert contar_filas("") == 0
    assert contar_columnas("") == 0