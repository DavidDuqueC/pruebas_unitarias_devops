import pytest
from src.conversor import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    celsius_a_kelvin,
    kelvin_a_celsius,
    metros_a_kilometros,
    kilometros_a_metros,
    libras_a_kilogramos,
    kilogramos_a_libras,
    galones_a_litros,
    litros_a_galones,
    millas_a_kilometros,
    kilometros_a_millas,
    pies_a_metros,
    metros_a_pies,
    onzas_a_gramos,
    gramos_a_onzas
)

def test_celsius_a_fahrenheit():
    # 1. Arrange + 2. Act + 3. Assert
    assert celsius_a_fahrenheit(25) == 77.0

def test_fahrenheit_a_celsius():
    # 1. Arrange + 2. Act + 3. Assert
    assert fahrenheit_a_celsius(77.0) == 25.0

def test_celsius_a_kelvin():
    # 1. Arrange + 2. Act + 3. Assert
    assert celsius_a_kelvin(0) == 273.15

def test_kelvin_a_celsius_valido_y_bug_negativo():
    # 1. Arrange + 2. Act + 3. Assert
    assert kelvin_a_celsius(273.15) == 0.0
    # BUG 1 expuesto: Esta prueba fallará porque la función actual no valida temperaturas Kelvin negativas (< 0)
    with pytest.raises(ValueError, match="La temperatura no puede ser menor a 0 Kelvin"):
        kelvin_a_celsius(-10)

def test_metros_a_kilometros():
    # 1. Arrange + 2. Act + 3. Assert
    assert metros_a_kilometros(1500) == 1.5

def test_kilometros_a_metros():
    # 1. Arrange + 2. Act + 3. Assert
    assert kilometros_a_metros(2) == 2000

def test_libras_a_kilogramos():
    # 1. Arrange + 2. Act + 3. Assert
    assert libras_a_kilogramos(10) == 4.53592

def test_kilogramos_a_libras():
    # 1. Arrange + 2. Act + 3. Assert
    assert kilogramos_a_libras(4.53592) == pytest.approx(10.0, 0.001)

def test_galones_y_litros():
    # 1. Arrange + 2. Act + 3. Assert
    assert galones_a_litros(1) == 3.78541
    assert litros_a_galones(3.78541) == pytest.approx(1.0, 0.001)

def test_millas_y_kilometros_con_bug():
    # 1. Arrange + 2. Act + 3. Assert
    assert millas_a_kilometros(1) == 1.60934
    # BUG 2 expuesto: 1 kilómetro debe ser aproximadamente 0.621371 millas (división), 
    # pero como el código multiplica, esto fallará y expondrá el bug.
    assert kilometros_a_millas(1) == pytest.approx(1 / 1.60934, 0.0001)

def test_pies_y_metros():
    # 1. Arrange + 2. Act + 3. Assert
    assert pies_a_metros(1) == 0.3048
    assert metros_a_pies(1) == 1 / 0.3048

def test_onzas_y_gramos():
    # 1. Arrange + 2. Act + 3. Assert
    assert onzas_a_gramos(1) == 28.3495
    assert gramos_a_onzas(28.3495) == pytest.approx(1.0, 0.001)

def test_distancia_negativa():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError, match="La distancia no puede ser negativa"):
        metros_a_kilometros(-500)

def test_peso_negativo():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError, match="El peso no puede ser negativo"):
        libras_a_kilogramos(-10)

def test_volumen_negativo():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError, match="El volumen no puede ser negativo"):
        galones_a_litros(-1)