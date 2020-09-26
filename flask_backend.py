from flask import Flask,render_template
import course

app = Flask(__name__)

@app.route('/')
def hello_world():
    all_schedules = course.create_schedules(["cs_204","al_102"])
    return render_template("schedule.html",all_schedules = all_schedules)

if __name__ == "__main__":
    app.run(debug=True)