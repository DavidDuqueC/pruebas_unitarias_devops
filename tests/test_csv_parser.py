import pytest
from src.csv_parser import (
    parse_csv_line, leer_csv_como_lista, 
    csv_a_diccionarios, validar_csv, contar_filas
)

def test_parse_csv_line():
    # 1. Arrange
    linea = "a,b,c"
    # 2. Act
    res = parse_csv_line(linea)
    # 3. Assert
    assert res == ["a", "b", "c"]

def test_leer_csv_como_lista():
    # 1. Arrange
    csv_content = "id,nombre\n1,Juan\n2,Ana"
    # 2. Act
    res = leer_csv_como_lista(csv_content)
    # 3. Assert
    assert len(res) == 3

def test_csv_a_diccionarios():
    # 1. Arrange
    csv_content = "nombre,edad\nJuan,25"
    # 2. Act
    res = csv_a_diccionarios(csv_content)
    # 3. Assert
    assert res == [{"nombre": "Juan", "edad": "25"}]

def test_validar_csv():
    # 1. Arrange
    csv_content = "a,b,c\n1,2,3\n4,5,6"
    # 2. Act
    res = validar_csv(csv_content)
    # 3. Assert
    assert res is True

def test_contar_filas():
    # 1. Arrange
    csv_content = "fila1\nfila2\nfila3"
    # 2. Act
    res = contar_filas(csv_content)
    # 3. Assert
    assert res == 3