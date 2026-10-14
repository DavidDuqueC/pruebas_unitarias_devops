import pytest
from src.utils import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    celsius_a_kelvin,
    kelvin_a_celsius,
    calcular_imc,
    categorizar_imc,
    calcular_edad,
    es_bisiesto,
    dias_en_mes,
    es_primo,
    mcd,
    mcm
)

def test_conversiones_temperatura_utils():
    # 1. Arrange + 2. Act + 3. Assert
    assert celsius_a_fahrenheit(0) == 32.0
    assert fahrenheit_a_celsius(32.0) == 0.0
    assert celsius_a_kelvin(0) == 273.15
    assert kelvin_a_celsius(273.15) == 0.0

def test_calcular_imc_exitoso():
    # 1. Arrange
    peso = 70.0
    altura = 1.75
    
    # 2. Act
    resultado = calcular_imc(peso, altura)
    
    # 3. Assert
    assert resultado == pytest.approx(22.857, 0.001)

def test_calcular_imc_valores_invalidos():
    # 1. Arrange + 2. Act + 3. Assert
    with pytest.raises(ValueError):
        calcular_imc(-10, 1.75)
    with pytest.raises(ValueError):
        calcular_imc(70, 0)

def test_categorizar_imc():
    # 1. Arrange + 2. Act + 3. Assert
    assert categorizar_imc(17.0) == "Bajo peso"
    assert categorizar_imc(22.0) == "Normal"
    assert categorizar_imc(27.0) == "Sobrepeso"
    assert categorizar_imc(32.0) == "Obesidad"

def test_calcular_edad():
    # 1. Arrange + 2. Act + 3. Assert
    assert calcular_edad(2000, 2026) == 26
    with pytest.raises(ValueError):
        calcular_edad(2030, 2026)

def test_es_bisiesto():
    # 1. Arrange + 2. Act + 3. Assert
    assert es_bisiesto(2024) is True
    assert es_bisiesto(2023) is False
    assert es_bisiesto(1900) is False  # Divisible por 100 pero no por 400
    assert es_bisiesto(2000) is True   # Divisible por 400

def test_dias_en_mes():
    # 1. Arrange + 2. Act + 3. Assert
    assert dias_en_mes(1, 2026) == 31  # Enero
    assert dias_en_mes(4, 2026) == 30  # Abril
    assert dias_en_mes(2, 2024) == 29  # Febrero bisiesto
    assert dias_en_mes(2, 2023) == 28  # Febrero normal
    with pytest.raises(ValueError):
        dias_en_mes(13, 2026)

def test_es_primo():
    # 1. Arrange + 2. Act + 3. Assert
    assert es_primo(2) is True
    assert es_primo(7) is True
    assert es_primo(11) is True
    assert es_primo(1) is False
    assert es_primo(4) is False
    assert es_primo(-5) is False

def test_mcd_y_mcm():
    # 1. Arrange + 2. Act + 3. Assert
    assert mcd(48, 18) == 6
    assert mcm(4, 5) == 20