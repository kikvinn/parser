from flask import Flask, render_template, request, jsonify
from parser import parse_timetable, GROUP
from db import init_db, insert_schedule, get_schedule_for_date
from datetime import datetime


app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/parser", methods=['POST'])
def parce():
    date = request.form['date'] # return str
    if not date:
        return 'Invalid input', 400
    try:
        date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y%W')
        schedule = parse_timetable(date, GROUP)
        
        insert_schedule(schedule)
        return '''Schedule added successfully. 
                  <a href="/schedule">View Schedule</a> | <a href="/">Go Back</a>''', 200
    except Exception as e:
        return f'Error: {str(e)}', 500
    
@app.route('/schedule', methods=['GET'])
def get_schedule():
    today = datetime.now().strftime('%Y-%m-%d')
    schedule = get_schedule_for_date(today)

    if not schedule:
        return render_template('schedule.html', schedule=None)

    return render_template('schedule.html', schedule=schedule)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
