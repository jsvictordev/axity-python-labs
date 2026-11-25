# Laboratorio 01.02 — Pre-commit y PEP 8

**Curso:** Python — Axity  
**Nivel:** Fundamental  
**Módulo:** 01 — Entorno y herramientas  
**Python:** 3.12  
**Gestor de dependencias:** Poetry

## 1. Objetivo

Configurar **pre-commit** para automatizar las validaciones de calidad del código Python antes de realizar commits en Git, utilizando Black, isort y Ruff.

El laboratorio permite identificar y corregir infracciones de las convenciones PEP 8, mantener un formato consistente y prevenir que se incorporen cambios que no cumplan las validaciones configuradas.

## 2. Herramientas utilizadas

| Herramienta | Propósito |
|---|---|
| Python 3.12 | Lenguaje de programación |
| Poetry | Gestión de dependencias y entornos virtuales |
| pre-commit | Ejecución automática de validaciones antes de un commit |
| Black | Formateo automático del código |
| isort | Ordenamiento de importaciones |
| Ruff | Análisis estático y detección de problemas de calidad |
| Git | Control de versiones |

## 3. Crear el proyecto

Desde la raíz del repositorio `axity-python-labs`:

```bash
mkdir -p fundamental/module-01-environment-and-tools
cd fundamental/module-01-environment-and-tools
```

Crear un proyecto Python independiente:

```bash
poetry new lab-01-02-precommit-pep8
cd lab-01-02-precommit-pep8
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

Instalar las dependencias del proyecto:

```bash
poetry install
```

Activar el entorno virtual:

```bash
source "$(poetry env info --path)/bin/activate"
```

Verificar la configuración:

```bash
poetry env info --path
which python
python --version
```

La ruta del entorno debe terminar en:

```text
lab-01-02-precommit-pep8/.venv
```

## 5. Instalar las herramientas de calidad

Agregar las herramientas como dependencias de desarrollo:

```bash
poetry add --group dev pre-commit black isort ruff
```

Verificar las instalaciones:

```bash
poetry run pre-commit --version
poetry run black --version
poetry run isort --version-number
poetry run ruff --version
```

Las dependencias quedan registradas en `pyproject.toml` y sus versiones resueltas en `poetry.lock`.

## 6. Configurar pre-commit

Crear el archivo de configuración:

```bash
touch .pre-commit-config.yaml
```

Agregar la siguiente configuración:

```yaml
repos:
  - repo: local
    hooks:
      - id: isort
        name: isort - Ordenar imports
        entry: fundamental/module-01-environment-and-tools/lab-01-02-precommit-pep8/.venv/bin/isort
        language: system
        files: ^fundamental/module-01-environment-and-tools/lab-01-02-precommit-pep8/.*\.py$
        pass_filenames: true

      - id: black
        name: black - Formatear Python
        entry: fundamental/module-01-environment-and-tools/lab-01-02-precommit-pep8/.venv/bin/black
        language: system
        files: ^fundamental/module-01-environment-and-tools/lab-01-02-precommit-pep8/.*\.py$
        pass_filenames: true

      - id: ruff
        name: ruff - Validar PEP 8
        entry: fundamental/module-01-environment-and-tools/lab-01-02-precommit-pep8/.venv/bin/ruff check
        language: system
        files: ^fundamental/module-01-environment-and-tools/lab-01-02-precommit-pep8/.*\.py$
        pass_filenames: true
```

### Explicación de la configuración

- `repo: local`: define hooks personalizados.
- `entry`: indica el ejecutable que utilizará cada hook.
- `language: system`: ejecuta las herramientas instaladas localmente.
- `files`: limita las validaciones a los archivos Python del laboratorio.
- `pass_filenames: true`: proporciona a cada herramienta las rutas de los archivos seleccionados.

Se utilizan ejecutables del entorno virtual porque pre-commit ejecuta los hooks desde la raíz del repositorio Git, no necesariamente desde el directorio del laboratorio.

**Nota:** Esta configuración está adaptada a la estructura de `axity-python-labs`. Si cambia la ubicación del laboratorio, deberán actualizarse las rutas.

### Validar el YAML

```bash
poetry run pre-commit validate-config .pre-commit-config.yaml
```

Si el comando termina sin errores, la configuración es válida.

## 7. Crear código con infracciones de estilo

Crear el archivo:

```bash
touch bad_code.py
```

Agregar código con problemas intencionales:

```python
import sys
import os
import json

def calcular_total(precio,cantidad):
    resultado=precio*cantidad
    return resultado

def saludar(nombre):
    print( "Hola "+nombre )

total=calcular_total(100,3)
saludar("Victor")
print(total)
```

### Problemas presentes

- Importaciones sin utilizar.
- Espacios incorrectos alrededor de operadores.
- Ausencia de espacios después de las comas.
- Separación incorrecta entre funciones.
- Formato inconsistente.

## 8. Ejecutar las herramientas manualmente

### isort

Ordenar las importaciones:

```bash
poetry run isort bad_code.py
```

### Black

Comprobar el formato:

```bash
poetry run black --check bad_code.py
```

Aplicar el formato:

```bash
poetry run black bad_code.py
```

### Ruff

Analizar el código:

```bash
poetry run ruff check bad_code.py
```

Aplicar correcciones automáticas disponibles:

```bash
poetry run ruff check --fix bad_code.py
```

Verificar nuevamente:

```bash
poetry run ruff check bad_code.py
```

Resultado esperado:

```text
All checks passed!
```

## 9. Ejecutar pre-commit

Agregar el archivo al índice de Git:

```bash
git add bad_code.py
```

Verificar que Git reconoce el archivo:

```bash
git status --short
git ls-files --full-name -- bad_code.py
git check-ignore -v bad_code.py
```

Obtener su ruta relativa a la raíz del repositorio:

```bash
FILE_PATH="$(git ls-files --full-name -- bad_code.py)"
echo "$FILE_PATH"
```

Ejecutar las validaciones:

```bash
poetry run pre-commit run \
  --files "$FILE_PATH" \
  --config .pre-commit-config.yaml \
  --verbose
```

También se puede ejecutar sobre todos los archivos rastreados que coincidan con la configuración:

```bash
poetry run pre-commit run --all-files \
  --config .pre-commit-config.yaml \
  --verbose
```

### Resultado observado durante el laboratorio

```text
isort - Ordenar imports..............................Passed

black - Formatear Python.............................Failed
- files were modified by this hook

ruff - Validar PEP 8.................................Passed

All checks passed!
```

El resultado `Failed` de Black no representa un error de instalación. Indica que Black modificó el archivo para corregir su formato.

Una vez aplicadas las correcciones:

```bash
git add bad_code.py
```

Repetir:

```bash
poetry run pre-commit run --all-files \
  --config .pre-commit-config.yaml
```

Resultado esperado:

```text
isort - Ordenar imports..............................Passed
black - Formatear Python.............................Passed
ruff - Validar PEP 8.................................Passed
```

## 10. Código corregido

Después de aplicar las herramientas, el código debe quedar similar al siguiente:

```python
def calcular_total(precio, cantidad):
    resultado = precio * cantidad
    return resultado


def saludar(nombre):
    print("Hola " + nombre)


total = calcular_total(100, 3)
saludar("Victor")
print(total)
```

## 11. Integración con Git

Instalar el hook para que se ejecute antes de cada commit:

```bash
poetry run pre-commit install \
  --config .pre-commit-config.yaml
```

Agregar los archivos del laboratorio:

```bash
git add .
```

Realizar el commit:

```bash
git commit -m "feat(lab-01-02): configure pre-commit and PEP 8 checks"
```

Durante el commit se ejecutarán automáticamente los hooks configurados.

Si alguno modifica archivos, se deberán revisar los cambios, agregarlos nuevamente y repetir el commit.

Publicar los cambios:

```bash
git push origin main
```

### Desinstalar el hook temporal

Dado que el repositorio contiene múltiples proyectos Poetry independientes, el hook puede retirarse después de demostrar su funcionamiento:

```bash
poetry run pre-commit uninstall
```

Esto no elimina la configuración ni las dependencias del laboratorio.

## 12. Problemas encontrados y soluciones

### Error 1. Configuración YAML inválida

```text
InvalidConfigError:
Expected a Config map but got a NoneType
```

**Causa:** El archivo `.pre-commit-config.yaml` estaba vacío o no contenía una estructura válida.

**Solución:** Agregar la configuración YAML y validarla:

```bash
poetry run pre-commit validate-config .pre-commit-config.yaml
```

### Error 2. No se encontraron archivos

```text
(no files to check)Skipped
```

**Causa:** Los hooks no encontraron archivos elegibles para procesar durante esa ejecución.

**Solución:** Verificar que Git reconoce el archivo, comprobar los filtros de la configuración y utilizar `--all-files` o `--files` con la ruta relativa a la raíz del repositorio.

### Error 3. Poetry no encontró pyproject.toml

```text
Poetry could not find a pyproject.toml file in
/Users/victor/Documents/axity/axity-python-labs
or its parents
```

**Causa:** Los hooks utilizaban `poetry run`, pero pre-commit los ejecutaba desde la raíz del repositorio, donde no existe un `pyproject.toml`.

**Solución:** Configurar las entradas de los hooks para utilizar directamente los ejecutables del `.venv` del laboratorio.

### Error 4. Entorno virtual incorrecto

La terminal inicialmente mostraba el entorno del laboratorio anterior:

```text
(lab-01-01-poetry-environment-py3.12)
```

**Solución:** Configurar y activar el entorno independiente del laboratorio 01.02:

```bash
poetry env use /opt/homebrew/bin/python3.12
source "$(poetry env info --path)/bin/activate"
```

Verificar:

```bash
poetry env info --path
```

## 13. Estructura del laboratorio

```text
lab-01-02-precommit-pep8/
├── .pre-commit-config.yaml
├── README.md
├── bad_code.py
├── pyproject.toml
├── poetry.lock
├── poetry.toml
├── src/
│   └── lab_01_02_precommit_pep8/
│       └── __init__.py
└── tests/
    └── __init__.py
```

El directorio `.venv/` debe excluirse del control de versiones.

## 14. Resultado del laboratorio

Se logró:

- Crear un proyecto independiente con Poetry y Python 3.12.
- Instalar Black, isort, Ruff y pre-commit.
- Configurar tres hooks locales.
- Identificar y corregir problemas de formato.
- Ejecutar correctamente isort y Ruff.
- Comprobar que Black modifica automáticamente archivos con formato incorrecto.
- Resolver problemas relacionados con las rutas de ejecución de Poetry y pre-commit.

La ejecución automática durante `git commit` se documenta como el paso final de integración.

## Autor

**Víctor José**  
Capacitación Python | Axity