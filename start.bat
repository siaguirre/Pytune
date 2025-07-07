@echo off
setlocal enabledelayedexpansion

echo Hola, Gracias por usar este proyecto :D Te comento un poco que va a hacer este script.
echo En primer lugar, te va a llevar a la pagina de colab para que levantes la IA. Es simple, segui los pasos que veas en el navegador.
echo Luego de levantarlo, volve aca y pega el link que te devolvio el Colab, es indispensable para que ande todo.
echo Luego de eso, se va a bajar todo lo necesario, necesitas pip y npm. Cuando finalice todo se va abrir en tu navegador el front
echo Eso es todo, a crear musica

set /p var_random=Apreta enter para comenzar

set URL=https://colab.research.google.com/github/siaguirre/Pytune/blob/main/backend/notebooks/app.ipynb
echo Abriendo navegador con: %URL%
start "" "%URL%"


set /p NGROK_URL=Por favor, ingresa la URL publica de ngrok (ej: https://xxxx.ngrok.io): 

echo Creando archivo .env con NGROK_URL...
echo NGROK_URL=%NGROK_URL%> .env

cd backend
echo Creando entorno virtual
python -m venv venv

echo Activando entorno virtual
call venv\Scripts\activate.bat

echo Instalando dependencias de Python
pip install -r requirements.txt

echo Ejecutando aplicación backend
start cmd /k "call venv\Scripts\activate.bat && py run.py"

cd ..


cd frontend

echo Instalando dependencias de Node
start cmd /k npm install

echo Ejecutando aplicacion frontend
start cmd /k "npm run dev"


set URL=http://localhost:5173
echo Abriendo navegador con: %URL%
start "" "%URL%"

endlocal
