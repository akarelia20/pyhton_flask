from flask import Flask

app= Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def hi_name(name):
    return f"Hi {name}!"

@app.route("/repeat/<int:num>/<string:word>")
def repeat(num, word):
    result = ""
    for i in range(0,num):
        result+= f"<h3>{word}<h3>"
    return result

@app.errorhandler(404)
def diffrent(error):
    return "Sorry! No response. Try again"


if __name__ == "__main__":
    app.run(debug=True)