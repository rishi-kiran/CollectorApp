from flask import Flask, render_template, request, flash, redirect, url_for
from db import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route("/")
def index():
    data = select()
    return render_template("home.html", output_data = data)

@app.route("/new", methods=["POST", "GET"])
def new():
    return render_template("new.html")

@app.route("/edit", methods=["POST", "GET"])
def edit():
    id = request.form['id_input']
    data = selectid(id)
    for row in data:
        name = str(row[0])
        academic = str(row[4])
        term = str(row[3])
        type = str(row[1])
        val = str(row[2])

    return render_template("new.html",id=id,name=name, academic=academic, term=term, type=type, val=val)

@app.route("/home")
def home():
    data = select()
    return render_template("home.html", output_data = data)

@app.route("/save", methods=["POST", "GET"])
def save():
    
    my_input = []
    name = str(request.form['name_input'])
    academic = str(request.form['academic_input'])
    term = str(request.form['term_input'])
    type = str(request.form['type_input'])
    val = str(request.form['value_input'])
    id = str(request.form['id_input'])
        
    if(request.form['submit_button'] == 'Cancel'):
        # name = ''
        # academic = ''
        # term = ''
        # type = ''
        # val = ''
        #data = select()
        #return render_template("result.html", output_data = data)
        return redirect(url_for('home'))
    
    if((str(request.form['name_input']) == '') or (str(request.form['value_input'])== '') or (str(request.form['type_input']) == '')):
        flash("Please enter required fields")
    else:
        #execute query
        my_input.append(name)
        my_input.append(academic)
        my_input.append(term)
        my_input.append(type)
        my_input.append(val)
        if(id != ''):
            my_input.append(id)
            flash(update(my_input))
        else:        
            flash(insert(my_input))
        name = ''
        academic = ''
        term = ''
        type = ''
        val = ''
        id = ''

    return render_template("new.html", name=name, academic=academic, term=term, type=type, val=val)