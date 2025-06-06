# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
    o "neutral". Este corresponde al nombre del directorio donde se
    encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """    # Importar las librerías necesarias
    import os          # Para manejar rutas y directorios del sistema operativo
    import pandas as pd    # Para crear y manejar DataFrames (tablas de datos)
    import zipfile     # Para descomprimir archivos ZIP

    # PASO 1: Descomprimir el archivo de datos
    # Definir la ruta donde se encuentra el archivo ZIP con los datos
    archivo_zip = 'files/input.zip'

    # Verificar si el archivo ZIP existe y descomprimirlo
    if os.path.exists(archivo_zip):
        # Abrir el archivo ZIP en modo lectura
        with zipfile.ZipFile(archivo_zip, 'r') as zip_archivo:
            # Extraer todos los archivos del ZIP al directorio actual ('.')
            zip_archivo.extractall('.')
    else:
        # Si el archivo no existe, mostrar error y terminar la función
        print(f"Error: No se encontró el archivo {archivo_zip}")
        return None, None

    # PASO 2: Preparar la carpeta de salida
    # Definir donde se guardarán los archivos CSV resultantes
    carpeta_salida = 'files/output'
    # Crear la carpeta si no existe (exist_ok=True evita error si ya existe)
    os.makedirs(carpeta_salida, exist_ok=True)

    # PASO 3: Definir los tipos de sentimientos que procesaremos
    # Estos nombres corresponden a las subcarpetas dentro de train/ y test/
    sentimientos = ['positive', 'negative', 'neutral']

    # PASO 4: Procesar los datos de entrenamiento
    # Crear una lista vacía para almacenar todos los datos de entrenamiento
    datos_entrenamiento = []
    
    # Recorrer cada tipo de sentimiento (positive, negative, neutral)
    for sentimiento in sentimientos:
        # Construir la ruta a la carpeta de cada sentimiento en train
        # Ejemplo: 'input/train/positive'
        carpeta_sentimiento = os.path.join('input', 'train', sentimiento)
        
        # Recorrer todos los archivos en esta carpeta de sentimiento
        for archivo_texto in os.listdir(carpeta_sentimiento):
            # Solo procesar archivos que terminen en .txt
            if archivo_texto.endswith('.txt'):
                # Construir la ruta completa al archivo
                # Ejemplo: 'input/train/positive/0000.txt'
                ruta_archivo = os.path.join(carpeta_sentimiento, archivo_texto)
                
                # Abrir y leer el contenido del archivo de texto
                with open(ruta_archivo, 'r') as archivo:
                    # Leer todo el contenido y quitar espacios al inicio/final
                    frase = archivo.read().strip()
                    # Agregar un diccionario con la frase y su sentimiento a la lista
                    datos_entrenamiento.append({'phrase': frase, 'target': sentimiento})

    # Convertir la lista de diccionarios en un DataFrame de pandas
    df_entrenamiento = pd.DataFrame(datos_entrenamiento)

    # PASO 5: Procesar los datos de prueba (mismo proceso que entrenamiento)
    # Crear una lista vacía para almacenar todos los datos de prueba
    datos_prueba = []
    
    # Recorrer cada tipo de sentimiento (positive, negative, neutral)
    for sentimiento in sentimientos:
        # Construir la ruta a la carpeta de cada sentimiento en test
        # Ejemplo: 'input/test/positive'
        carpeta_sentimiento = os.path.join('input', 'test', sentimiento)
        
        # Recorrer todos los archivos en esta carpeta de sentimiento
        for archivo_texto in os.listdir(carpeta_sentimiento):
            # Solo procesar archivos que terminen en .txt
            if archivo_texto.endswith('.txt'):
                # Construir la ruta completa al archivo
                # Ejemplo: 'input/test/positive/0000.txt'
                ruta_archivo = os.path.join(carpeta_sentimiento, archivo_texto)
                
                # Abrir y leer el contenido del archivo de texto
                with open(ruta_archivo, 'r') as archivo:
                    # Leer todo el contenido y quitar espacios al inicio/final
                    frase = archivo.read().strip()
                    # Agregar un diccionario con la frase y su sentimiento a la lista
                    datos_prueba.append({'phrase': frase, 'target': sentimiento})

    # Convertir la lista de diccionarios en un DataFrame de pandas
    df_prueba = pd.DataFrame(datos_prueba)

    # PASO 6: Guardar los DataFrames como archivos CSV
    # Guardar el dataset de entrenamiento como CSV (sin índices de fila)
    df_entrenamiento.to_csv(os.path.join(carpeta_salida, 'train_dataset.csv'), index=False)
    # Guardar el dataset de prueba como CSV (sin índices de fila)
    df_prueba.to_csv(os.path.join(carpeta_salida, 'test_dataset.csv'), index=False)

    # PASO 7: Retornar los DataFrames creados
    # Devolver ambos DataFrames para que puedan ser utilizados si es necesario
    return df_entrenamiento, df_prueba