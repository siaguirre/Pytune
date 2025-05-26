# 🎵 Pytune - Generador de Música Algorítmica

### Proyecto de Algoritmos y Estructura de Datos 1 — Grupo 3

[🚀 Abrir en Colab](https://colab.research.google.com/github/siaguirre/Pytune/blob/main/notebooks/app.ipynb#scrollTo=QXtcpW3Vg1xp)

---

## 📌 ¿Cómo correr el proyecto?

1. Cloná este repositorio.
2. Abrí el archivo `app.ipynb` en Google Colab y ejecutalo.
3. El sistema solicitará una clave para establecer el túnel con **Ngrok**. Esta clave se encuentra disponible en el chat de Teams del TP.
4. Una vez iniciado Ngrok, copiá la URL que devuelve y pegala en el archivo `.env`, en la variable `GRONK_URL`.
5. Antes de ejecutar `app.py` por primera vez:

   ```bash
   python -m venv nombre_ambiente
   pip install -r requirements.txt
   ```
6. Ejecutá `app.py`.

---

## 👥 Participantes

* Aguirre, Simón
* Mónaco, Ezequiel
* Romero, Valentín
* Podestá, Jerónimo

---

## 🎯 Introducción

Este proyecto consiste en un **generador de música algorítmica con Inteligencia Artificial**. El objetivo es desarrollar una herramienta que, mediante reglas y modelos de IA, permita la creación de melodías accesibles incluso para quienes no tengan conocimientos avanzados de teoría musical.

---

## 🧹 Alcance del Producto

El sistema permite:

* Generar melodías y patrones musicales de forma algorítmica.
* Personalizar las composiciones según estilos y emociones.
* Exportar la música generada en formato `.WAV`.
* Integrarse con una interfaz gráfica amigable.

---

## ✅ Requisitos Funcionales

La generación musical se basa en **MusicGen**, un motor que emplea modelos preentrenados capaces de interpretar prompts de texto (y eventualmente de audio) para crear piezas musicales.

---

## 📘 Implementación de temas de la materia

| Tema                                                   | Aplicación en el proyecto                                              |
| ------------------------------------------------------ | ---------------------------------------------------------------------- |
| Listas, matrices, diccionarios, archivos de texto/JSON | Guardado y persistencia de prompts generados                           |
| `map`, `filter`, `reduce`                              | Manipulación avanzada de los prompts (tono, duración, velocidad, etc.) |
| Expresiones regulares                                  | Búsqueda optimizada entre prompts históricos                           |
| Manejo de excepciones                                  | Validación y control de errores                                        |
| Pruebas unitarias                                      | Verificación del correcto funcionamiento de los módulos                |

---

## ✍️ Ingreso de Prompts

El sistema permite dos formas de generar un prompt musical:

1. A través de botones que definen ambiente, estilo e instrumentos.
2. Escribiendo directamente un prompt personalizado.

---

## 📦 Entregables

* **40%**: Generador de melodías básico con exportación funcional.
* **80%**: Integración de la interfaz gráfica + guardado de prompts + pruebas unitarias.
* **100%**: Proyecto completo con:

  * Interfaz gráfica refinada
  * Modularización del código
  * Excepciones implementadas
  * Recolección y persistencia de prompts
  * Personalización avanzada

---
