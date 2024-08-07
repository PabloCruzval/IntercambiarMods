# Intercambiar Mods

Este proyecto es un programa para gestionar y mover archivos de mods entre la carpeta de mods activos y una para guardarlos.

## Estructura del Proyecto

- **app.py**: Archivo principal que maneja la lógica del menú y las interacciones del usuario.
- **functions.py**: Contiene funciones auxiliares utilizadas por `app.py` para gestionar los archivos y los paquetes.

## Requisitos

- Python 3.x
- pathlib
- os
- shutil
- time

## Instalación

1. Clona el repositorio a tu máquina local:

   ```bash
   git clone https://github.com/PabloCruzval/IntercambiarMods
   cd IntercambiarMods
   ```

2. Asegúrate de tener Python 3.x instalado en tu sistema.

## Uso

1. Cambia los directorios de las variables `ACTIVEFOLDER` por el directorio en el cual el juego cargue los mods, y cambia el directorio de `OTHERFOLDERS` a una carpeta en la cual quieras guardar los otros mods.

2. En el archivo `functions.py` se encuentra una tupla con las extensiones de los mods, si tus mods tienen otra extension, modifica la tupla.

3. Ejecuta el script principal:

   ```bash
   python app.py
   ```

4. Sigue las instrucciones del menú para gestionar tus mods.
