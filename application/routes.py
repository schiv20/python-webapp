import datetime
from functools import wraps

import jwt
from flask import render_template, request, flash, jsonify, current_app
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
    return render_template('login.html', title='Login',  email=email, password=password)

@app.route("/login_page")
def login_page():
    return render_template('login.html', title='Login')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Token is missing"}), 401

        token = auth_header.split(" ", 1)[1]
        try:
            jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated

def generate_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    secret = current_app.config.get("SECRET_KEY")
    if not isinstance(secret, str) or not secret:
        raise RuntimeError("SECRET_KEY must be a non-empty string")

    token = jwt.encode(payload, secret, algorithm="HS256")
    return token if isinstance(token, str) else token.decode("utf-8")

@app.route("/login", methods=["POST"])
def login():
    # Accept JSON or form-encoded
    data = request.get_json(silent=True) or request.form
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    ca = Connector()
    if ca.verify_user_by_password(email, password):
        token = generate_token(email)
        print("successfully logged in")
        print(token)
        return jsonify({"token": token}), 200
        return render_template('home.html', title="Home")
    else:
        print("login failed")
        return jsonify({"error": "Invalid credentials"}), 401
