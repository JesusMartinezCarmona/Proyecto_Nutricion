# 🍎 Nutri-Quiz: Sistema Experto Gamificado (GUI) 🚀

**Nutri-Quiz** es una aplicación de escritorio con **Interfaz Gráfica de Usuario (GUI)** diseñada como un videojuego educativo (Quiz). Su objetivo es evaluar y orientar los hábitos alimenticios de niños de 8 a 12 años basándose en normas oficiales de salud (NOM-043), utilizando técnicas de **Inteligencia Artificial Simbólica**.

## 📋 Descripción del Proyecto

A diferencia de la versión anterior basada en consola, esta versión implementa una experiencia **gamificada** e interactiva. El sistema actúa como un "Nutriólogo Virtual" que:

1. Interactúa mediante botones, colores y animaciones.

2. Ofrece retroalimentación inmediata (tips nutricionales).

3. Utiliza un **Motor de Inferencia de Encadenamiento hacia Adelante** para diagnosticar la dieta.

Este proyecto fue desarrollado para la materia de **Programación Lógica Funcional**, demostrando cómo la lógica computacional puede aplicarse en software educativo moderno.

## 🎯 Objetivos

1. **Implementar un Sistema Experto:** Utilizar una base de conocimientos (Reglas y Hechos) para simular el razonamiento de un experto en nutrición.

2. **Mejorar la Experiencia de Usuario (UX):** Migrar de una interfaz de texto a una gráfica (GUI) usando `tkinter` para mantener la atención del público infantil.

3. **Aplicar Lógica de Primer Orden:** Utilizar el algoritmo *Modus Ponendo Ponens* para inferir conclusiones a partir de las respuestas del usuario.

4. **Educación Incidental:** Enseñar conceptos de salud mientras el usuario juega, mediante pantallas de "Tips" entre preguntas.

## ⚙️ Arquitectura del Sistema

El código está estructurado en tres capas principales dentro de un único módulo de Python:

### 1. El Cerebro (Lógica y Conocimiento) 🧠

Es el núcleo del Sistema Experto. No depende de la interfaz gráfica.

* **Base de Conocimientos (`REGLAS`):** Una lista de diccionarios que define la lógica nutricional.

  * *Ejemplo:* `SI (come frutas) Y (come verduras) ENTONCES (buen consumo vegetal)`.

* **Motor de Inferencia (`motor_inferencia_adelante`):** Algoritmo de **Forward Chaining**. Recorre cíclicamente las reglas, comparando las premisas con los hechos acumulados para derivar nuevos hechos hasta llegar a una conclusión final.

### 2. La Interfaz (Vista y Control) 🎨

Implementada con la librería estándar `tkinter`.

* **Clase `NutriQuizGame`:** Gestiona el flujo del juego, la ventana principal, y la coordinación entre preguntas y motor de inferencia.

* **Clase `BotonOpcion`:** Una clase personalizada que hereda de `tk.Button` para agregar interactividad (efectos *hover* de cambio de color y tamaño).

### 3. Gamificación y Feedback 🎮

Elementos añadidos para el refuerzo positivo:

* **Mascota Animada:** Un canvas que renderiza una animación de rebote (bucle simple).

* **Efecto de Máquina de Escribir:** El texto de las preguntas aparece carácter por carácter.

* **Sistema de Partículas (Confeti):** Al obtener un resultado positivo, se genera una animación matemática de partículas aleatorias para celebrar.

## 🚀 Características Técnicas

* **Paradigma:** Orientado a Objetos (para la GUI) + Lógico/Funcional (para el Motor).

* **Librerías:**

  * `tkinter`: Renderizado de ventanas y widgets.

  * `time`: Control de animaciones.

  * `random`: Aleatoriedad en colores de confeti y selección de tips.

* **Algoritmo de Inferencia:**

```

# Lógica simplificada del motor

while hechos\_nuevos:
for regla in reglas:
if premisas\_cumplidas(regla) and conclusion\_no\_conocida:
agregar\_hecho(regla['conclusion'])

```

## 📸 Guía de Usuario

1. **Inicio:** El niño es recibido por el "Nutri-Bot" animado.

2. **Preguntas:** Responde 10 preguntas sobre situaciones cotidianas (Recreo, Cena, Antojos).

3. **Tips Intermedios:** Entre preguntas, aparecerán datos curiosos ("¿Sabías qué?"). El usuario debe presionar "¡Entendido!" para avanzar, fomentando la lectura.

4. **Diagnóstico:** Al final, el sistema procesa todas las respuestas y emite un veredicto:

 * 🏆 **Nutri-Ninja:** Dieta Balanceada.

 * ✨ **Vas bien:** Dieta con áreas de oportunidad.

 * ⚠️ **Alerta:** Dieta desbalanceada (exceso de azúcar/grasas).

## 🛠️ Instalación y Ejecución

**Requisitos:**

* Tener instalado **Python 3.x**.

* (Opcional) Un entorno virtual activado.

**Pasos:**

1. Clona este repositorio o descarga el archivo `nutri_quiz.py`.

2. Ejecuta el script desde tu terminal:

```

python nutri_quiz.py

```
```
