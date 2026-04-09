# codigo en pytest para validar los rangos de temperatura, humedad y velocidad del viento
#para validar que los valores ingresados por el usuario estén dentro de los rangos #permitidos
#para ejecutar las pruebas, se puede usar el comando " python -m pytest o pytest tests/test_rangos.py" en la #terminal

from src.validation import (
    validar_temperatura,
    validar_humedad_nivel,
    validar_viento_velocidad
)


def test_validar_temperatura_valores_validos():
    assert validar_temperatura(-15) is True
    assert validar_temperatura(0) is True
    assert validar_temperatura(25) is True
    assert validar_temperatura(50) is True


def test_validar_temperatura_valores_invalidos():
    assert validar_temperatura(-16) is False
    assert validar_temperatura(51) is False


def test_validar_humedad_nivel_valores_validos():
    assert validar_humedad_nivel(0) is True
    assert validar_humedad_nivel(50) is True
    assert validar_humedad_nivel(100) is True


def test_validar_humedad_nivel_valores_invalidos():
    assert validar_humedad_nivel(-1) is False
    assert validar_humedad_nivel(101) is False


def test_validar_viento_velocidad_valores_validos():
    assert validar_viento_velocidad(1) is True
    assert validar_viento_velocidad(80) is True
    assert validar_viento_velocidad(130) is True


def test_validar_viento_velocidad_valores_invalidos():
    assert validar_viento_velocidad(0) is False
    assert validar_viento_velocidad(-5) is False
    assert validar_viento_velocidad(131) is False
