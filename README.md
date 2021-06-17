# Seguimiento de flota

![inove_logo](https://inove.com.ar/wp-content/uploads/2020/03/cropped-3-1.png)

Este proyecto consiste en analizar los movimientos de una flota de vehículos, ya sea vehículos de transporte, de pasajeros, de encomienda o de delivery.
El objetivo es analizar la información de los viajes realizados.

**Los viajes son guardados en un archivo csv, los viajes son guardados manualmente por el administrador de la app. Los datos que se obtienen por cada viaje son los siguientes:**

- Fecha de salida
- Patente del vehículo
- Empresa
- Tiempo recorrido (en minutos)
- Recaudación
- Fecha de llegada (sin uso aún)
- latitud (fuera de servicio)
- longitud (fuera de servicio)

## Propósito del proyecto

El propósito del proyecto es poner a prueba los conocimientos dados en el primer módulo (python inicial) del curso brindado por INOVE ARG.

Otros propósitos del proyecto son:
- Profundizar github
- Aprender a crear un readme
- Aprender a armar un programa de forma ordenada y limpia
- Mejorar la lógica de la programación
- Transformarla en un servicio para producción
- Seguir aprendiendo!

## Características del proyecto

_En este sector del readme se nombran y explican las funcionalidades del proyecto:_

### Inicio del programa:
**Al ejecutar el programa mostrará una interfaz gráfica como la siguente**
![Inicio]()

- Si presiona la tecla **a** entra como administrador
- Si presiona la tecla **v** entra como visitante
- Si presiona la tecla **x** sale del programa

- Iniciar sesion como administrador:
    - Usuario: **Admin**
    - Contraseña: **Contraseña123**

- Funciones de administrador:
    - Modificar un registro
    - Crear un registro
    - Eliminar un registro
    - Analizar un registro

- Funciones de visitante:
    - Analizar un registro

### (1) Modificar un registro:

**Esta función permite cambiar los datos de un campo determinado**

#### Modo de uso:

- **(1)** Ingresar la fecha del registro que desea modificar
![Inicio]()
- **(2)** Ingresar el campo que desea modificar
![Inicio]()
- **(3)** Ingresar los datos nuevos
![Inicio]()

### (2) Crear un registro:

**Esta función permite crear un nuevo registro de flota**

#### Modo de uso:

- **(1)** Completar los campos correspondientes del registro
![Inicio]()

### (3) Eliminar un registro:

**Esta función permite eliminar un registro de flota**

#### Modo de uso:

- **(1)** Ingresar la fecha del registro que desea eliminar
![Inicio]()

### (4) Analizar un registro:

**Esta función permite analizar un registro de flota**
![Inicio]()

## Aclaraciones:

- Se puede salir en cualquier momento al escribir "exit"
- El proyecto puede sufrir actualizaciones en un futuro
- Cualquier consulta al correo **nahuelarrascaeta22@gmail.com**

## Pre-requisitos:

Este programa no tiene ningún pre-requisito, puedes descargar el repositorio y jugar con él

## Instalación:

Para usar el programa debes descargar el repositorio github

## Archivos que contiene el proyecto:

Este proyecto consta de 4 archivos y un directorio con las imágenes para el readme

- (1) Pictures **=> Directorio donde se almacenan imágenes de la ejecución del programa**
- (2) Diagrama_proyector_inicial_PY_inove.jpg **=> diagrama del proyecto**
- (3) main.py **=> Archivo principal para ejecutar el programa**
- (4) README.md **=> archivo de información del proyecto**
- (5) seguimiento_flota.csv **=> archivo csv en donde se almacenan los registros de viaje**

## Herramientas que se usaron en el proyecto:

- librería csv
- https://app.diagrams.net/

## Progreso de la construcción del programa
**_Actualización de repositorio todos los Martes_**

- Fecha de inicio: **Martes 27 de Abril del 2021**
    - Se crearon los archivos necesarios y se implementó el inicio del programa.

- Siguiente actualización: **Martes 11 de Mayo del 2021**
    - Se crearon dos funciones para administrador:
        - modify_record
        - create_record
    - También se creó el archivo csv para guardar los análisis.

- Siguiente actualización: **Martes 18 de Mayo del 2021**
    - Se terminó de crear la función (crear registro)
    - Se implementaron cambios pequeños en el código

- Siguiente actualización: **Martes 25 de Mayo del 2021**
    - Se creó una función para recorrer el archivo csv hasta encontrar la fila deseada
    - Se creó la función:
        - record_delete
    - Se modificó la función:
        - modify_record
    - Se añadieron funcionalidades a main

- Siguiente actualización: **Martes 01 de Junio del 2021**
    - Se modificó la función:
        - get_date
        - modify_record
        - record_delete
    - Se creó la función:
        - analyze_record

- Entrega final: **Martes 08 de Junio del 2021**
    - Se modificó la función:
        - get_date
        - modify_record
        - record_delete
        - create_record
        - analyze_record
    - Se creó la función:
        - examp_fieldnames

## Autor:
Nahuel_A

## Licencia: