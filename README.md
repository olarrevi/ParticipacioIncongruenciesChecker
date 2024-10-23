# ParticipacioIncongruenciesChecker

Este proyecto tiene como objetivo identificar y corregir inconsistencias en los datos de participación pública recopilados en diferentes estudios y paneles usando python. La herramienta permite verificar diversas reglas de validación para asegurar la coherencia de los datos y generar informes de las incongruencias encontradas.

## Características

- Carga de datos desde archivos `.sav` y `.xlsx`.
- Verificación de reglas predefinidas para detectar inconsistencias en los datos.
- Generación de informes de incongruencias en formato Excel.
- Ordenación de los resultados por población y responsable.
- Creación de hipervínculos en el informe para facilitar la navegación.
- Filtrado de casos especiales a través de un archivo de excepciones.

## Estructura del proyecto

- `incongruencies.py`: Script principal que carga los datos, aplica las reglas y genera el informe de inconsistencias.
- `participacio_final.py`: Archivo que contiene las variables y las reglas de validación.
- `excepciones.py`: Diccionario con los casos especiales que deben ser excluidos del análisis.
- `data/`: Carpeta que contiene los archivos de datos (`snPART_2024.sav`, `responsables.xlsx`).
- `output/`: Carpeta donde se guardan los resultados generados (`incongruencias_por_regla.xlsx`).

## Reglas de validación

Las reglas de validación se aplican a los datos para identificar inconsistencias. Algunos ejemplos incluyen:
- Verificación de que las sumas de ciertos valores sean mayores a 0 si se han marcado como realizadas.
- Comparación de datos entre diferentes fuentes (estudio web y panel).
- Validación de las diferencias aceptables en el número de entidades según la población.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/ParticipacioIncongruenciesChecker.git
    ```

2. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

3. Añade los archivos de datos en la carpeta `data/`.

## Uso

Ejecuta el script principal para generar el informe de incongruencias:
```bash
python incongruencies.py
