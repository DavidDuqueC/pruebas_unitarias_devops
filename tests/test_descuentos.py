import pytest
from src.descuentos import calcular_descuento

def test_calcular_descuento_estandar():
    # 1. Arrange
    precio_base = 100.0
    es_vip = False

    # 2. Act
    resultado = calcular_descuento(precio_base, es_vip)

    # 3. Assert
    assert resultado >= 0.0

def test_calcular_descuento_vip():
    # 1. Arrange
    precio_base = 100.0

    # 2. Act
    resultado_vip = calcular_descuento(precio_base, True)
    resultado_normal = calcular_descuento(precio_base, False)

    # 3. Assert
    assert resultado_vip > resultado_normal

def test_calcular_descuento_precio_negativo_lanza_error():
    # 1. Arrange
    precio_invalido = -50.0

    # 2. Act + 3. Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio_invalido, False)