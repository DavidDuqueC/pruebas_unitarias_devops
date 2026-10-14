import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_por_volumen,
    descuento_cumulativo,
    descuento_apilado
)

def test_aplicar_descuento_valido():
    # 1. Arrange
    precio = 200.0
    porcentaje = 10.0
    
    # 2. Act
    resultado = aplicar_descuento(precio, porcentaje)
    
    # 3. Assert
    assert resultado == 180.0

def test_aplicar_descuento_precio_negativo():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        aplicar_descuento(-50.0, 10.0)

def test_aplicar_descuento_porcentaje_invalido():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError, match="El porcentaje debe estar entre 0 y 100"):
        aplicar_descuento(100.0, 150.0)
    with pytest.raises(ValueError, match="El porcentaje debe estar entre 0 y 100"):
        aplicar_descuento(100.0, -5.0)

def test_calcular_descuento_estandar():
    # 1. Arrange
    precio_base = 100.0
    porcentaje = 20.0

    # 2. Act
    resultado = calcular_descuento(precio_base, porcentaje)

    # 3. Assert
    assert resultado == 20.0

def test_calcular_precio_final_con_bug():
    # 1. Arrange
    precio = 100.0
    impuesto = 19.0
    descuento = 10.0 # Precio con descuento = 90. Impuesto correcto sobre 90 = 17.1 -> Total = 107.1
    
    # 2. Act
    resultado = calcular_precio_final(precio, impuesto, descuento)
    
    # 3. Assert (BUG 1 expuesto: el impuesto se calcula sobre el precio original 100 -> 90 + 19 = 109)
    # Dejamos la aserción con el valor correcto matemático para que la prueba falle y documente el bug.
    assert resultado == pytest.approx(107.1, 0.01)

def test_calcular_precio_final_validaciones():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        calcular_precio_final(-10, 19, 10)
    with pytest.raises(ValueError):
        calcular_precio_final(100, -5, 10)
    with pytest.raises(ValueError):
        calcular_precio_final(100, 19, 110)

def test_descuento_por_volumen_rangos():
    # 1. Arrange + 2. Act + 3. Assert
    # Menos de 10 unidades (0% descuento)
    assert descuento_por_volumen(5, 10.0) == 50.0
    # Entre 10 y 19 unidades (5% descuento)
    assert descuento_por_volumen(10, 10.0) == 95.0
    # Entre 20 y 49 unidades (10% descuento)
    assert descuento_por_volumen(20, 10.0) == 180.0
    # Entre 50 y 99 unidades (15% descuento)
    assert descuento_por_volumen(50, 10.0) == 425.0
    # 100 o más unidades (20% descuento)
    assert descuento_por_volumen(100, 10.0) == 800.0

def test_descuento_por_volumen_negativo():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        descuento_por_volumen(-2, 10.0)
    with pytest.raises(ValueError):
        descuento_por_volumen(10, -5.0)

def test_descuento_cumulativo():
    # 1. Arrange
    precio = 100.0
    descuentos = [10.0, 20.0] # 100 -> 90 -> 72
    
    # 2. Act
    resultado = descuento_cumulativo(precio, descuentos)
    
    # 3. Assert
    assert resultado == 72.0
    assert descuento_cumulativo(100.0, []) == 100.0

def test_descuento_cumulativo_invalido():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        descuento_cumulativo(100.0, [110.0])

def test_descuento_apilado_con_bug():
    # 1. Arrange
    precio = 100.0
    descuentos = [60.0, 50.0] # Suma 110% (> 100%)
    
    # 2. Act & 3. Assert (BUG 2 expuesto: no valida si excede el 100%)
    with pytest.raises(ValueError, match="El descuento total no puede superar el 100%"):
        descuento_apilado(precio, descuentos)