from flask import Flask, render_template

app = Flask(__name__)

#render templates with 3 blue boxes
@app.route("/play")
def play():
    return render_template("index.html", num=3, color="aqua")

# displays mentioned number of boxes in the route for example if route is "local:5000/play/8" displays 8 boxes
@app.route("/play/<int:num>")
def num_of_times(num):
    return render_template("index.html", num=num, color="aqua")

# render a template with x number of boxes with provided color value
@app.route("/play/<int:num>/<string:color>")
def color(num,color):
    return render_template("index.html", num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)
