from flask import Flask, render_template, request, redirect, url_for, jsonify
from parser import parse_timetable, GROUP

app = Flask(__name__)

@app.route("/")
def index():
    """Главная страница с данными из базы."""
    return render_template("index.html")

@app.route("/parser", methods=['POST'])
def parce():
    day = request.form['date'] # return str
    day = tuple(map(int, day.split('-')))
    html = parse_timetable(day, GROUP)
    
    return jsonify(html)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
