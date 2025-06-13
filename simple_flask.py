from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Educational institute</h1></html>"

@app.route("/courses")
def courses():
    return "Devops, Linux, python, docker"

@app.route("/syllabus")
def syllabus():
    return render_template("syllabus.html")

@app.route('/fees')
def fees():
    return "Free for people with high curosity"
if __name__=="__main__":
    app.run(debug=True)

