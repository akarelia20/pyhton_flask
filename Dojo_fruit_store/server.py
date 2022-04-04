from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)  
app.secret_key = "abcd"

@app.route('/') #GET        
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])  #POST       
def checkout():
    session["strawberry"] = request.form["strawberry"]
    session["raspberry"] = request.form["raspberry"]
    session["blackberry"] = request.form["blackberry"]
    session["apple"] = request.form["apple"]
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["student_id"] = request.form["student_id"]
    session["num_fruits"] = int(request.form["strawberry"]) + int(request.form["raspberry"]) + int(request.form["apple"]) + int(request.form["blackberry"])
    session["date"] = datetime.now().strftime("%x")
    print(session)
    return redirect('/conformation')

@app.route('/conformation') #GET
def result():
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    images= ["/static/img/apple.png", "/static/img/blackberry.png", "/static/img/raspberry.png", "/static/img/strawberry.png"]
    # print(images[0])
    return render_template("fruits.html", images=images)

if __name__=="__main__":   
    app.run(debug=True)    