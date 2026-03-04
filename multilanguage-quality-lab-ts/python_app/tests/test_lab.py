
# TODO: Escribe pruebas unitarias para es_palindromo y suma.
# Sugerencias:
# - "radar" -> True, "anita lava la tina" -> True, "python" -> False, "" -> True, "Radar" -> True
# - suma(2,3) -> 5; suma(0,5) -> 5; suma(-2,3) -> 1

from python_app.palindromo import es_palindromo
from python_app.utils import suma


def test_ejemplo_siembra():
    assert True


def test_es_palindromo_casos_basicos():
    # cadenas simples
    assert es_palindromo("radar") is True
    assert es_palindromo("python") is False


def test_es_palindromo_espacios_y_mayusculas():
    # ignora espacios y mayúsculas
    assert es_palindromo("anita lava la tina") is True
    assert es_palindromo("") is True
    assert es_palindromo("Radar") is True


def test_suma_valores():
    assert suma(2, 3) == 5
    assert suma(0, 5) == 5
    assert suma(-2, 3) == 1

