from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'JoeIsTheMan'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    session['logged'] = False
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    print(request.form['email'])
    print(request.form)

    goodForm = True


    if len(request.form['email']) < 1:
        flash("<span style='color: red'>Email required</span>")
        goodForm = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("<span style='color: red'>Email really not valid</span>")
        goodForm = False
    else:
        flash("<span style='color: green'>fluffy message</span>")
        session['logged'] = True

    

    if goodForm == False:
        return redirect('/')
    else:
        return redirect('/home')

@app.route('/home')
def home():
    if 'logged' in session:
        if session['logged'] == False:
            flash("please submit an email")
            return redirect('/')
        else:
            return render_template('success.html')
    return redired('/')




if __name__ == "__main__":
    app.run(debug=True)