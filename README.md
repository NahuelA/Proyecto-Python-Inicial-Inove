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
- Fecha de llegada

## Propósito del proyecto

El propósito del proyecto es poner a prueba los conocimientos dados en el primer módulo (python inicial) del curso brindado por INOVE ARG.

Otros propósitos del proyecto son:
- Profundizar github
- Aprender a crear un readme
- Aprender a armar un programa de forma ordenada y limpia
- Mejorar la lógica de la programación
- Seguir aprendiendo!

## Características del proyecto

En este sector del readme se nombran y explican las funciones del programa:

Funcionalidades admitidas al iniciar como administrador:

### (1) Modificar un registro de viaje:

_Esta función permite cambiar los datos de un campo determinado_

#### Modo de uso

Al elegir dicha función, el usuario **admin** debe ingresar la fecha del registro guardado. Luego ingresar el campo deseado para modificarlo, ingresar los nuevos datos y listo.

INSERTAR IMAGEN DE LA EJECUCIÓN

### (2) Crear un registro:



## Progreso de la construcción del programa
**_Actualización de repositorio todos los Martes_**

- Fecha de inicio: **Martes 27 de Abril del 2021**
    - Se crearon los archivos necesarios y se implementó el inicio del programa.

- Siguiente actualización: **Martes 11 de Mayo del 2021**
    - Se crearon dos funciones para administrador:
        - Modificar registro
        - Crear registro
    - También se creó el archivo csv para guardar los análisis.

- Siguiente actualización: **Martes 18 de Mayo del 2021**
    - Se terminó de crear la función (crear registro)
    - Se implementaron cambios pequeños en el código

- Siguiente actualización: **Martes 25 de Mayo del 2021**
    - Se creó una función para recorrer el archivo csv hasta encontrar la fila deseada
    - Se creó la función:
        - eliminar registro
    - Se modificó la función:
        - modificar registro
    - Se añadieron funcionalidades a main
- Siguiente actualización: **Martes 01 de Junio del 2021**
    - Se modificó la función:
        - get_date
        - modify_record
        - record_delete
    - Se creó la función:
        - verify_record