# Registro e inicio de sesión

Aplicación Flask con registro de usuarios, inicio de sesión y cierre de sesión,
organizada según la estructura `flask_app` del proyecto.

## Requisitos

- Python 3.13
- MySQL

## Configuración

1. Crea un entorno virtual e instala las dependencias:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install Flask==3.1.2 mysql-connector-python==9.4.0 python-dotenv==1.1.1
   ```

2. Copia `.env.example` a `.env` y configura la clave secreta y las credenciales
   de MySQL. La aplicación carga automáticamente ese archivo al iniciar.

3. Crea la base de datos y la tabla:

   ```powershell
   mysql -u root -p < flask_app\bd\schema.sql
   ```

4. Inicia la aplicación desde la carpeta raíz:

   ```powershell
   py -m flask_app.server
   ```

Abre `http://127.0.0.1:5000`. Las contraseñas se guardan con hash y las consultas
usan parámetros para evitar concatenar valores del usuario en SQL.
