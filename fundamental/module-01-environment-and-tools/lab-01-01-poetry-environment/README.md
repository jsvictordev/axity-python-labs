# Laboratorio 01.01 — Poetry y entorno virtual

**Curso:** Python — Axity  
**Nivel:** Fundamental  
**Módulo:** 01 — Entorno y herramientas  
**Python:** 3.12

## 1. Objetivo

Configurar un proyecto Python utilizando Poetry para la gestión de dependencias y entornos virtuales, e instalar herramientas de calidad de código: Black, isort y Ruff.

## 2. Requisitos previos

- macOS con Homebrew
- Git
- Python 3.12
- Poetry

### Instalar Python 3.12

```bash
brew install python@3.12
```

Verificar la instalación:

```bash
/opt/homebrew/bin/python3.12 --version
which python3.12
```

### Instalar Poetry

```bash
brew install poetry
```

Verificar:

```bash
poetry --version
which poetry
```

## 3. Crear el proyecto

Desde la raíz del repositorio `axity-python-labs`:

```bash
mkdir -p fundamental/module-01-environment
cd fundamental/module-01-environment
```

Crear el proyecto:

```bash
poetry new lab-01-01-poetry-environment
cd lab-01-01-poetry-environment
```

## 4. Configurar el entorno virtual

Configurar Poetry para crear el entorno virtual dentro del proyecto:

```bash
poetry config virtualenvs.in-project true --local
```

Seleccionar Python 3.12:

```bash
poetry env use /opt/homebrew/bin/python3.12
```

Verificar:

```bash
poetry env info
```

Activar el entorno virtual:

```bash
source "$(poetry env info --path)/bin/activate"
```

Comprobar la versión de Python:

```bash
python --version
```

Resultado esperado:

```text
Python 3.12.16
```

## 5. Instalar herramientas de calidad

Instalar Black, isort y Ruff como dependencias de desarrollo:

```bash
poetry add --group dev black isort ruff
```

Verificar las instalaciones:

```bash
poetry run black --version
poetry run isort --version-number
poetry run ruff --version
```

### Función de cada herramienta

| Herramienta | Descripción |
|---|---|
| Black | Formatea automáticamente el código Python |
| isort | Organiza y ordena las importaciones |
| Ruff | Analiza el código y detecta problemas de calidad y estilo |

## 6. Crear un archivo de prueba

Crear el archivo:

```bash
touch example.py
```

Agregar el siguiente código intencionalmente desordenado:

```python
import sys
import os

def greet(name):
    print( "Hola, " + name )
```

Este código contiene problemas de formato e importaciones sin utilizar.

## 7. Ejecutar herramientas de calidad

Ordenar importaciones:

```bash
poetry run isort example.py
```

Formatear código:

```bash
poetry run black example.py
```

Analizar el código:

```bash
poetry run ruff check example.py
```

Corregir automáticamente los problemas detectados por Ruff:

```bash
poetry run ruff check --fix example.py
```

Validar nuevamente:

```bash
poetry run ruff check example.py
```

Resultado esperado:

```text
All checks passed!
```

## 8. Verificar el entorno y las dependencias

Consultar información del entorno virtual:

```bash
poetry env info
```

Listar las dependencias de desarrollo:

```bash
poetry show --only dev
```

Validar el código:

```bash
poetry run ruff check example.py
```

## 9. Estructura del proyecto

```text
lab-01-01-poetry-environment/
├── README.md
├── pyproject.toml
├── poetry.lock
├── poetry.toml
├── example.py
├── src/
│   └── lab_01_01_poetry_environment/
│       └── __init__.py
└── tests/
    └── __init__.py
```

El directorio `.venv/` se genera localmente y no debe incluirse en Git.

## 10. Buenas prácticas

- Utilizar Python 3.12.
- Administrar las dependencias mediante Poetry.
- Mantener un entorno virtual independiente por laboratorio.
- Utilizar Black, isort y Ruff para mantener la calidad del código.
- Versionar `pyproject.toml` y `poetry.lock`.
- Excluir `.venv/`, cachés y archivos temporales del repositorio.

## 11. Resultado esperado

Al finalizar el laboratorio se contará con:

- Un proyecto Python creado con Poetry.
- Un entorno virtual configurado con Python 3.12.
- Black, isort y Ruff instalados.
- Un archivo Python formateado y validado.
- Dependencias documentadas en `pyproject.toml` y `poetry.lock`.

## Autor

**Víctor José**  
Capacitación Python | Axity