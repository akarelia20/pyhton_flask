from flask import Flask, render_template,session, redirect, request
from env import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/')
def index():
    #stores the total visits
    if 'total_visits' not in session:
        session['total_visits'] = 0
    # session is a form of dict, so in thsi case counters are stored in keyword 'visits' 
    # if session is not active/present then visit= 0, helps wiith the '/destroy_session/' route
    if 'counter' not in session: 
        session['counter'] = 0
    else:
        #if session is active meaning if the user had visited this page prior then add 1
        session['counter'] += 1
        session['total_visits'] += 1
    return render_template("index.html")

@app.route('/destroy_session/')
def reset():
    #clears the currently active session and redirects to index.html and wipes down the data fom counter.
    session.pop('counter')
    return redirect('/')

@app.route("/add2/")
def add2():
    #adds 2 to the counter and total visits
    session['total_visits'] += 1
    session['counter'] += 1 # 1 is added here and 1 adds after redirecting to index.html
    return redirect ('/') 

@app.route('/add_num_times',methods=['POST'])
def add_num_of_times():
    session['total_visits'] = (session['total_visits']-1) + int(request.form['num'])
    #adds the number inputted in the HTML, for example if the number is 2 and current counter=1 
    # then it subtracts 1 from current counter (counter= 0) and adds the inputted number 2 (counter=2) and
    # redirects the page to index.html where 1 gets added (counter=3)
    session['counter']= (session['counter']-1)+ int(request.form['num'])
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)



