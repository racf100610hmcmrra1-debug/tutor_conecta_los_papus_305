from flask import Flask, render_template

app = Flask(__name__)


# Pantalla de bienvenida
@app.route('/')
def inicio():
    return render_template('index.html')


# Crear cuenta (al enviar el formulario abre el panel)
@app.route('/registro')
def registro():
    return render_template('registro.html')


# Iniciar sesión (al enviar el formulario abre el panel)
@app.route('/login')
def inicio_sesion():
    return render_template('login.html')


# Panel principal con las opciones
@app.route('/panel')
def panel_principal():
    return render_template('panel.html')


@app.route('/alumnos')
def registro_alumnos():
    return render_template('alumnos.html')


@app.route('/calificaciones')
def calificaciones():
    return render_template('calificaciones.html')


@app.route('/asistencias')
def asistencias():
    return render_template('asistencias.html')


@app.route('/inasistencias')
def inasistencias():
    return render_template('inasistencias.html')


@app.route('/reportes')
def reportes():
    return render_template('reportes.html')


@app.route('/quejas')
def quejas():
    return render_template('quejas.html')


if __name__ == '__main__':
    app.run(debug=True)