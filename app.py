# Importamos las librerias para trabajar con Flask
from flask import Flask, render_template


# Creamos la aplicación con parámetro tmaplate, para obtener los achivos html
app = Flask(__name__, template_folder='templates')

# Se crea una ruta para la pagina principal
@app.route('/')
def index():
    # Se retorna el archivo html principal
    return render_template('index.html')


# Se ejeuta la aplicacion en modo debug, esto para que se pueda ver los cambios en el codigo sin necesidad de reiniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)
