import os
from flask import Flask, render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from form import Form


basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = 'softsecretkey'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'database.db')
app.config['SQLALCHEMY_TRACK_MODIFIATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/client_reg')
def client_reg():
    form = Form()
    return render_template('client_reg.html', form =form)