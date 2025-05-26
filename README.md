[🚀Abrir en Colab](https://colab.research.google.com/github/siaguirre/Pytune/blob/main/notebooks/app.ipynb#scrollTo=QXtcpW3Vg1xp)

# ¿Cómo correr el proyecto?
1. Cloná el repositorio
2. Cargá el archivo app.ipynb como notebook en Colab y ejecutalo
3. Te va a pedir una clave para crear el túnel con Ngrok, esta clave está subida al chat de Teams del TP.
4. Ngrok va a devolver una URL, copiarla y pegarla en el .env en GRONK_URL.
5. Antes de iniciar app.py por primera vez, crear un entorno y realizar una instalacion de las dependencias. 
> python -m venv nombre_ambiente
> pip install -r requirements.txt
6. Ejecutar app.py.

# Proyecto Pytune - Grupo 3

## Algoritmos y Estructura de Datos 1

### Participantes
- Aguirre, Simón
- Mónaco, Ezequiel
- Romero, Valentín
- Podestá, Jerónimo

---

## Introducción

Este documento detalla el proyecto de un generador de música algorítmica con Inteligencia Artificial. El objetivo principal es desarrollar un sistema capaz de generar melodías basadas en reglas predefinidas utilizando modelos de IA. Se buscará crear una herramienta accesible para usuarios sin conocimientos avanzados de teoría musical, facilitando la composición de piezas musicales de manera algorítmica.

---

## Alcance del Producto

El sistema permitirá:
- Generar melodías y patrones musicales de forma algorítmica.
- Ofrecer opciones de personalización según diferentes estilos y emociones.
- Exportar la música en formato `.WAV` para su uso en aplicaciones externas.
- Integrarse con una interfaz gráfica.

---

## Requisitos funcionales

La generación de música se llevará a cabo utilizando **MusicGen**, un generador de música algorítmica que cuenta con distintos modelos preentrenados. Con uno de estos modelos, podremos generar música basado en un prompt de texto e incluso de audio que cargue el usuario en el sistema.

### Implementación de temas de la materia:

| Tema | Implementación en el proyecto |
|------|------------------------------|
| Listas avanzadas, matrices y diccionarios en conjunto con guardado en archivos de texto/JSON | Guardado de prompts previos para poder acceder a ellos luego de generarlos, incluso tras cerrar la aplicación |
| Map, filter, reduce | Modificación de prompts avanzado, con velocidades, tonos, duraciones, además de la idea principal |
| Expresiones regulares | Búsqueda avanzada en prompts pasados basado en texto |
| Excepciones | Validación y prevención de errores |
| Pruebas unitarias | Creación de archivos de prueba para asegurar los correctos cambios en el proyecto |

### ¿Cómo se ingresan estos prompts?

Existen dos formas principales:
1. Utilizando botones que definan ambientes, estilos e instrumentos.
2. Mediante un prompt generado enteramente por el usuario.

---

## Entregables

- **40%**: Implementación del generador básico de melodías con opciones de exportación.
- **80%**: Integración de la interfaz gráfica con guardado de prompts y creación de pruebas unitarias.
- **100%**: Proyecto terminado, entregado en conjunto con todas las pruebas unitarias aprobadas, modularización y uso de excepciones. Interfaz gráfica pulida, con persistencia y recolección de prompts previos, personalización de los prompts.