from flask import Flask, render_template, redirect, session, request
from env import KEY

app = Flask(__name__)
app.secret_key = KEY

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("results.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)

