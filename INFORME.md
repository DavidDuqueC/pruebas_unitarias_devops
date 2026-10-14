# Informe Técnico: Taller de Pruebas Unitarias y DevOps

**Autor:** David Duque Cardona  
**Programa:** Administración de Sistemas Informáticos - Universidad Nacional de Colombia (Sede Manizales)  
**Herramientas:** Python 3.12, `pytest`, `pytest-cov`, Git  

---

## 1. Análisis por Módulo (Criterios de Prueba)

El diseño de las pruebas unitarias se basó en el patrón **AAA (Arrange-Act-Assert)**, buscando probar los de valores límite y manejo de excepciones sobre las funciones de python (hice pruebas para todos los componentes):

*   **`autenticacion.py`**: Se validaron contratos estrictos de seguridad, longitudes mínimas de credenciales, manejo de tokens hexadecimales y saneamiento de entradas ante posibles inyecciones.
*   **`calculadora.py`**: Enfoque en robustez matemática, validación de dominios cerrados (como raíces reales) y operaciones sobre estructuras numéricas.
*   **`conversor.py`**: Verificación de factores de conversión física exacta y restricciones de dominios termodinámicos (cero absoluto en Kelvin).
*   **`descuentos.py`**: Pruebas sobre rangos porcentuales válidos, cálculos cumulativos, descuentos por volumen y límites superiores de apilamiento.
*   **`fibonacci.py`**: Validación de casos base iterativos/recursivos y manejo correcto de errores ante entradas negativas.
*   **`validador.py`**: Pruebas de expresiones regulares y formatos estrictos para correos, teléfonos, cédulas y validación lógica de fechas.
*   **`utils.py` & `manipulador_texto.py`**: Pruebas funcionales de transformaciones de cadenas, manejo de espacios múltiples, palíndromos y algoritmos utilitarios.
*   **`csv_parser.py`**: Pruebas de parsing tabular, validación de integridad estructural de filas y columnas.

---

## 2. Registro y Análisis de Bugs Seleccionados (13 Bugs encontrados, 3 corregidos)

De acuerdo con la estrategia de desarrollo propuesta en el correo, documenté los fallos mediante pruebas específicas antes de aplicar las correcciones para cada uno:

| Módulo / Función | Entrada que revela el defecto | Comportamiento Erróneo (Actual) | Comportamiento Esperado | Estado |
| :--- | :--- | :--- | :--- | :--- |
| **`calculadora.py`** <br>`raiz_cuadrada` | `n = -4` | Retorna un número complejo o un cálculo impreciso sin control de dominio. | Lanzar una excepción explícita `ValueError`. | Documentado y Corregido |
| **`calculadora.py`** <br>`minimo` | `numeros = [4, 2, 9, 1, 7]` | Retorna `0` debido a un error de inicialización en el acumulador. | Retornar el elemento mínimo real de la lista (`1`). | Documentado y Corregido |
| **`conversor.py`** <br>`kilometros_a_millas` | `km = 1` | Aplica multiplicación por `1.60934` en lugar de división (operación inversa). | Aplicar división correcta (`1 / 1.60934` $\approx 0.6213$ millas). | Documentado y Corregido |


## 3. Evidencias de Ejecución y Cobertura

### A. Ejecución de Pruebas y Exposición de Bugs ANTES DE CORREGIRLOS
La ejecución de `pytest` evidencia el comportamiento esperado de las pruebas orientadas a contratos y los fallos controlados que exponen los defectos lógicos del código base:

(venv) aevd4123@aevd4123-ThinkPad-E14-Gen-3:~/Documentos/pruebas_unitarias_devops$ pytest --cov=src --cov-report=term-missing
================================================ test session starts =================================================
platform linux -- Python 3.12.3, pytest-8.0.0, pluggy-1.6.0
rootdir: /home/aevd4123/Documentos/pruebas_unitarias_devops
plugins: cov-4.0.0
collected 97 items                                                                                                   

---------- coverage: platform linux, python 3.12.3-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/__init__.py                0      0   100%
src/autenticacion.py          42      5    88%   37-38, 51, 57-58
src/calculadora.py            42      7    83%   57, 62-64, 68-70
src/conversor.py              56      9    84%   32, 44, 56, 62, 68, 75, 81, 87, 93
src/csv_parser.py             76      7    91%   17, 56, 66, 82, 89, 98, 124
src/descuentos.py             58      5    91%   20, 23, 75, 92, 95
src/fibonacci.py              42      1    98%   70
src/manipulador_texto.py      93      8    91%   43, 52, 89, 94, 106, 117, 140, 143
src/procesador_texto.py       49     23    53%   9, 17, 25, 31, 38-41, 46, 51-53, 57-59, 63-66, 70-75, 80
src/utils.py                  53      0   100%
src/validador.py              64      2    97%   18, 26
--------------------------------------------------------
TOTAL                        575     67    88%

============================================== short test summary info ===============================================
FAILED tests/test_calculadora.py::test_raiz_cuadrada_negativa - Failed: DID NOT RAISE <class 'ValueError'>
FAILED tests/test_calculadora.py::test_maximo_y_minimo - assert 0 == 1
FAILED tests/test_conversor.py::test_kelvin_a_celsius_valido_y_bug_negativo - Failed: DID NOT RAISE <class 'ValueError'>
FAILED tests/test_conversor.py::test_millas_y_kilometros_con_bug - assert 1.60934 == 0.6213727366498067 ± 6.2e-05
FAILED tests/test_csv_parser.py::test_extraer_y_filtrar_columna - AssertionError: assert 1 == 2
FAILED tests/test_descuentos.py::test_calcular_precio_final_con_bug - assert 109.0 == 107.1 ± 1.1e+00
FAILED tests/test_descuentos.py::test_descuento_apilado_con_bug - AssertionError: Regex pattern did not match.
FAILED tests/test_manipulador_texto.py::test_es_palindromo_con_bug - AssertionError: assert False is True
FAILED tests/test_manipulador_texto.py::test_eliminar_duplicados - AssertionError: assert 'progamcin' == 'progamin'
FAILED tests/test_manipulador_texto.py::test_dividir_en_palabras_con_bug - AssertionError: assert ['uno', '', 'dos'] == ['uno', 'dos']
FAILED tests/test_manipulador_texto.py::test_normalizar_espacios_y_truncar - AssertionError: assert 'Hola ...' == 'Hola...'
FAILED tests/test_validador.py::test_validar_email_invalidos - AssertionError: assert True is False
FAILED tests/test_validador.py::test_validar_fecha_valida_y_bug - assert True is False
=========================================== 13 failed, 84 passed in 0.28s ============================================


### B. Ejecución de Pruebas y Exposición de Bugs DESPUÉS DE CORREGIR LOS 3 REQUERIDOS
(venv) aevd4123@aevd4123-ThinkPad-E14-Gen-3:~/Documentos/pruebas_unitarias_devops$ pytest --cov=src --cov-report=term-missing
================================================ test session starts =================================================
platform linux -- Python 3.12.3, pytest-8.0.0, pluggy-1.6.0
rootdir: /home/aevd4123/Documentos/pruebas_unitarias_devops
plugins: cov-4.0.0
collected 97 items                                                                                                   

---------- coverage: platform linux, python 3.12.3-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/__init__.py                0      0   100%
src/autenticacion.py          42      5    88%   37-38, 51, 57-58
src/calculadora.py            44      6    86%   64-66, 70-72
src/conversor.py              56      9    84%   32, 44, 56, 62, 68, 75, 81, 87, 93
src/csv_parser.py             76      7    91%   17, 56, 66, 82, 89, 98, 124
src/descuentos.py             58      5    91%   20, 23, 75, 92, 95
src/fibonacci.py              42      1    98%   70
src/manipulador_texto.py      93      8    91%   43, 52, 89, 94, 106, 117, 140, 143
src/procesador_texto.py       49     23    53%   9, 17, 25, 31, 38-41, 46, 51-53, 57-59, 63-66, 70-75, 80
src/utils.py                  53      0   100%
src/validador.py              64      2    97%   18, 26
--------------------------------------------------------
TOTAL                        577     66    89%

============================================== short test summary info ===============================================
FAILED tests/test_conversor.py::test_kelvin_a_celsius_valido_y_bug_negativo - Failed: DID NOT RAISE <class 'ValueError'>
FAILED tests/test_csv_parser.py::test_extraer_y_filtrar_columna - AssertionError: assert 1 == 2
FAILED tests/test_descuentos.py::test_calcular_precio_final_con_bug - assert 109.0 == 107.1 ± 1.1e+00
FAILED tests/test_descuentos.py::test_descuento_apilado_con_bug - AssertionError: Regex pattern did not match.
FAILED tests/test_manipulador_texto.py::test_es_palindromo_con_bug - AssertionError: assert False is True
FAILED tests/test_manipulador_texto.py::test_eliminar_duplicados - AssertionError: assert 'progamcin' == 'progamin'
FAILED tests/test_manipulador_texto.py::test_dividir_en_palabras_con_bug - AssertionError: assert ['uno', '', 'dos'] == ['uno', 'dos']
FAILED tests/test_manipulador_texto.py::test_normalizar_espacios_y_truncar - AssertionError: assert 'Hola ...' == 'Hola...'
FAILED tests/test_validador.py::test_validar_email_invalidos - AssertionError: assert True is False
FAILED tests/test_validador.py::test_validar_fecha_valida_y_bug - assert True is False
=========================================== 10 failed, 87 passed in 0.24s ============================================
