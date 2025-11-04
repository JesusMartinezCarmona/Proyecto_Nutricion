# 🍎 Nutri-Quiz Lógico (Versión de Consola) 🖥️

## 1. Descripción del Proyecto

**Nutri-Quiz Lógico** es una aplicación de consola desarrollada en Python. El proyecto está diseñado como un quiz interactivo para niños de 8 a 12 años, con el objetivo de evaluar y orientar sus hábitos alimenticios basándose en los principios del "Plato del Buen Comer".

Este proyecto fue desarrollado para la materia de **Programación Lógica**, aplicando conceptos de **bases de conocimiento** y un **motor de inferencia de encadenamiento hacia adelante (forward chaining)**.

## 2. Objetivo

El objetivo principal es utilizar la programación lógica para crear un sistema simple que pueda:
1.  **Recopilar hechos** sobre los hábitos alimenticios de un niño a través de preguntas cerradas en la terminal.
2.  **Procesar estos hechos** utilizando una base de conocimiento (reglas lógicas).
3.  **Inferir una conclusión** (diagnóstico) sobre la calidad de su dieta.
4.  **Presentar una retroalimentación** positiva (felicitación) o constructiva (orientación) en un lenguaje sencillo.

## 3. Componentes del Proyecto

El código se estructura en tres partes fundamentales que simulan un sistema experto básico:

### a. Interfaz de Consola (Funciones `input`/`print`)
Toda la interacción con el usuario se maneja a través de funciones nativas de Python en la terminal.
* **`hacer_quiz()`**: Esta función se encarga de imprimir cada pregunta y sus opciones numeradas (ej. 1, 2, 3).
* **`input()`**: Captura la respuesta del usuario. El niño solo debe escribir el número de la opción que elige.
* **Validación de Entrada**: El código incluye un bucle `while True` con un bloque `try/except` para asegurar que el usuario ingrese un número válido que corresponda a una opción.
* **`mostrar_resultado_consola()`**: Una vez que el motor de inferencia termina, esta función imprime el título y el mensaje de retroalimentación de forma clara y formateada.

### b. Base de Conocimientos (Las `REGLAS`)
Es el "cerebro" del sistema. Es una lista de diccionarios donde cada diccionario representa una regla lógica simple:

```python
# Ejemplo de una regla
{'if': ['consume_bebidas_azucaradas'], 'then': 'riesgo_alto_azucar'}