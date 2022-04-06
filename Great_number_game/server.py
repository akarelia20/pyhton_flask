from flask import Flask, render_template, session, redirect, request
import random
from env import KEY

app= Flask(__name__)
app.secret_key= KEY

@app.route('/')
def index():
    if 'attempts' not in session:
        session['attempts'] = 0
    if 'random' not in session:
        session['random'] = random.randint(1, 100) 
        print(session['random'])
    return render_template("index.html" )

@app.route('/process', methods=['POST'])
def process():
    session['guess'] = int(request.form['guess'])
    session['attempts'] += 1
    print(session)
    return redirect("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)