from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("index.html",x=8, y=8, color1="red", color2="black")

@app.route("/4")
def eight_four():
    return render_template ("index.html", x=8 ,y=4, color1="red", color2="black" )

@app.route("/<int:horizontal>/<int:vertical>")
def random(horizontal,vertical):
    return render_template("index.html", x= horizontal, y= vertical, color1="red", color2="black")

@app.route("/<int:horizontal>/<int:vertical>/<string:color1>/<string:color2>")
def color(horizontal,vertical, color1 ,color2 ):
    return render_template ("index.html", x= horizontal, y= vertical, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)
