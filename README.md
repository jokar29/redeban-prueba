# redeban-prueba


## Descripción

Este proyecto implementa un microservicio en FastAPI para guardar, consultar y actualizar parámetros en una base de datos Mysql.

## Requisitos

- Python 3.9
- MySql

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/jokar29/redeban-prueba.git
    cd __pycache__\app
    ```

2. Crear y activar un entorno virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configurar la base de datos en `database.py`:
    ```python
    DATABASE_URL = "postgresql://root:@localhost/dbprueba-redeban"
    ```

5. Ejecutar la aplicación:
    ```bash
    uvicorn main:app --reload
    ```

