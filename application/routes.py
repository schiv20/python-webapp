from flask import render_template, request, flash
import random
from application import app
from application.connector import Connector


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/welcome/<string:name>')
def welcome(name='Team'):
    return render_template('welcome.html', title="Welcome", name=name.title(), group='Everyone')


@app.route('/joke')
def joke():
    ca  = Connector()
    joke = ca.extract_joke()
    num_of_jokes = ca.extract_num_of_jokes()
    return render_template('joke.html', title="Joke Time", joke_question=joke[0], joke_answer=joke[1], number_of_jokes=num_of_jokes)
       
@app.route('/hello')
def hello():
    return render_template('hello.html', title='Hello')

@app.route("/register_page")
def register_page():
    return render_template('register.html', title='Register')

@app.route("/register", methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    ca = Connector()
    ca.add_user(email, password)
    return render_template('register.html', title='Register',  email=email, password=password)
