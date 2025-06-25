Paso 0. Abrir la terminal desde el directorio del repo

Ejecuta el siguiente comando para crear el entorno virtual:
python -m venv venv

Paso 1. Activa el entorno virtual:

En Windows:
venv\Scripts\activate

En macOS/Linux:
source venv/bin/activate

Se deberia ver como
 (venv) /tu_path> $ 
 
Paso 2. Usar requirements.txt para Instalar Dependencias Si necesitas instalar todas las dependencias listadas en el archivo requirements.txt, ejecuta:
pip install -r requirements.txt

Si quiere desactivar el entorno virtual:
deactivate 

EL archivo lex.py contiene la definicion de los tokens, el archivo yacc.py contiene la definicion e las reglas de sintaxis que debe seguir nuestro lenguaje asignado y el archivo main.py es un archivo donde se encuentra la aplicacion a ejecutar, entonces desde la consola ubicacado en la ruta de nuestro proyeto puedes correr el comando:
python main.py

Al ejecutar este comando se solicitara un nombre de archivo. Aqui debe ingresarse el nombre del archivo en el que esta cargado el codigo de SQL que desea traducirse a XQL.
![image](https://github.com/user-attachments/assets/f30d94d2-15c1-4123-a046-bf87e963dcf6)




