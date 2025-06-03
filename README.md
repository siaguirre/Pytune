# 🎵 Pytune - Generador de Música Algorítmica

### Proyecto de Algoritmos y Estructura de Datos 1 — Grupo 3

Una aplicación completa que combina **Frontend React** + **Backend Flask** para generar música usando Inteligencia Artificial.

---

## 🏗️ Arquitectura del Proyecto

```
Pytune/
├── frontend/          # Aplicación React con TypeScript
│   ├── src/
│   ├── public/
│   └── package.json
├── backend/           # API Flask
│   ├── app/
│   ├── notebooks/
│   ├── templates/
│   ├── output/
│   ├── requirements.txt
│   └── run.py
└── README.md
```

---

## 🚀 Cómo ejecutar el proyecto

### 📋 Prerrequisitos

- **Python 3.10+** con pip
- **Node.js 18+** con npm
- **Git**

### 🔧 Configuración del Backend (Flask)

1. **Navegar al directorio del backend:**
   ```bash
   cd backend
   ```

2. **Instalar dependencias de Python:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el servidor Flask:**
   ```bash
   python run.py
   ```
   
   El backend se ejecutará en `http://127.0.0.1:5000`

### 🎨 Configuración del Frontend (React)

1. **Navegar al directorio del frontend:**
   ```bash
   cd frontend
   ```

2. **Instalar dependencias de Node.js:**
   ```bash
   npm install
   ```

3. **Ejecutar la aplicación React:**
   ```bash
   npm run dev
   ```
   
   El frontend se ejecutará en `http://localhost:5173`

### 🌐 Acceso a la Aplicación

Una vez que ambos servidores estén ejecutándose:
- Abre tu navegador en `http://localhost:5173`
- La aplicación React se comunicará automáticamente con el backend Flask

---

## 🛠️ Stack Tecnológico

### Frontend
- **React 19** con TypeScript
- **Vite** como bundler
- **TailwindCSS** para estilos
- **FontAwesome** para íconos
- **Axios** para peticiones HTTP

### Backend
- **Flask 3.1** como framework web
- **Flask-CORS** para manejo de CORS
- **Requests** para peticiones HTTP
- **Python-dotenv** para variables de entorno

---

## 👥 Participantes

* Aguirre, Simón
* Mónaco, Ezequiel
* Romero, Valentín
* Podestá, Jerónimo

---

## 🎯 Introducción

Este proyecto consiste en un **generador de música algorítmica con Inteligencia Artificial**. El objetivo es desarrollar una herramienta que, mediante reglas y modelos de IA, permita la creación de melodías accesibles incluso para quienes no tengan conocimientos avanzados de teoría musical.

La aplicación cuenta con una **interfaz web moderna y responsiva** desarrollada en React, que se comunica con un **backend robusto en Flask** para procesar las peticiones de generación musical.

---

## 🧹 Alcance del Producto

El sistema permite:

* 🎼 Generar melodías y patrones musicales de forma algorítmica
* 🎨 Personalizar las composiciones según estilos, instrumentos y emociones
* 💾 Exportar la música generada en formato `.WAV`
* 📱 Interfaz web responsiva y amigable
* 📝 Historial de prompts con persistencia local
* 🔄 Comunicación en tiempo real entre frontend y backend

---

## ✅ Funcionalidades Principales

### 🎵 Generación Musical
- **Motor MusicGen**: Emplea modelos preentrenados para interpretar prompts de texto
- **Prompts personalizados**: Escribir descripciones libres de la música deseada
- **Selección guiada**: Interfaz con dropdowns para género, instrumento y estado de ánimo

### 💻 Interfaz de Usuario
- **Diseño moderno**: UI/UX con TailwindCSS
- **Ejemplos predefinidos**: Tarjetas con prompts de ejemplo
- **Historial dinámico**: Guarda y reutiliza prompts anteriores
- **Estados de carga**: Feedback visual durante la generación
- **Descarga automática**: Los archivos de audio se descargan automáticamente

### 🔧 Backend Robusto
- **API RESTful**: Endpoints bien definidos para comunicación
- **Manejo de errores**: Validación y respuestas de error apropiadas
- **CORS configurado**: Permite comunicación frontend-backend
- **Modular**: Código organizado en módulos reutilizables

---

## 📘 Implementación de temas de la materia

| Tema                                                   | Aplicación en el proyecto                                              |
| ------------------------------------------------------ | ---------------------------------------------------------------------- |
| Listas, matrices, diccionarios, archivos de texto/JSON | Guardado y persistencia de prompts generados                           |
| `map`, `filter`, `reduce`                              | Manipulación avanzada de los prompts (tono, duración, velocidad, etc.) |
| Expresiones regulares                                  | Búsqueda optimizada entre prompts históricos                           |
| Manejo de excepciones                                  | Validación y control de errores en backend y frontend                  |
| Pruebas unitarias                                      | Verificación del correcto funcionamiento de los módulos                |
| Programación orientada a objetos                      | Estructura modular del backend Flask                                   |
| Manejo de archivos                                     | Lectura/escritura de configuraciones y logs                           |

---

## 🎛️ Configuración Avanzada

### Variables de Entorno (Backend)
Crear archivo `.env` en la carpeta `backend/`:
```env
FLASK_ENV=development
FLASK_DEBUG=True
NGROK_URL=https://tu-url-ngrok.com/generate_music
```
---

## 📦 Estructura de Entregables

* **40%**: Generador de melodías básico con exportación funcional ✅
* **80%**: Integración de la interfaz gráfica + guardado de prompts + pruebas unitarias ✅
* **100%**: Proyecto completo con:
  * ✅ Interfaz web moderna y responsiva
  * ✅ Modularización del código frontend y backend
  * ✅ Manejo de excepciones implementado
  * ✅ Recolección y persistencia de prompts
  * ✅ Personalización avanzada de la música
  * ✅ Arquitectura escalable frontend-backend

---

*🎵 ¡Disfruta creando música con Pytune! 🎵*
