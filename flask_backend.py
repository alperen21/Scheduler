from flask import Flask,render_template,session,request,redirect,url_for
from wtforms import Form, BooleanField, StringField, PasswordField, validators
import course

app = Flask(__name__)
app.secret_key = "hello"

class ScheduleForm(Form):
    lectures = StringField()

@app.route('/',methods=["POST","GET"])
def index():
    form = ScheduleForm(request.form)
    if request.method == "POST":
        selected_lectures = form.lectures.data
        session["selected_lectures"] = selected_lectures

        return redirect(url_for("schedules"))
    else:   
        return render_template("index.html",form=form)

@app.route('/schedules')
def schedules():

    if "selected_lectures" in session:
        selected_lectures = session["selected_lectures"]

    all_schedules = course.create_schedules(selected_lectures)
    return render_template("schedule.html",all_schedules=all_schedules)

if __name__ == "__main__":
    app.run(debug=True)