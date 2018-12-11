from flask import Flask, render_template, url_for
applicaiton = Flask(__name__)

@applicaiton.route("/")
@applicaiton.route("/home")
def home():
    return render_template('layout.html')

@applicaiton.route("/checkin_project")
def checkin_project():
    return render_template("checkin_project.html")

@applicaiton.route("/unit_testing")
def unit_testing():
    return render_template("unit_testing.html")

if __name__ == '__main__':
    applicaiton.run(host="0.0.0.0", debug=True, port=80)
