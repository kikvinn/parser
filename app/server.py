from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Инициализация базы данных


@app.route("/")
def index():
    """Главная страница с данными из базы."""
    return render_template("index.html")


@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
