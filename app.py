from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Dati di accesso hard-coded (per semplicità)
USERNAME = "admin"
PASSWORD = "admin"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            # Autenticazione riuscita, reindirizza a una pagina di benvenuto
            return redirect(url_for('welcome'))
        else:
            # Autenticazione fallita, mostra un messaggio di errore
            error = "Credenziali non valide. Riprova."
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return "Benvenuto, admin!"

if __name__ == '__main__':
    app.run(debug=True)
