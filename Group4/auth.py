
from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import Client
from flask_login import login_user, current_user, logout_user, login_required
from .forms import RegistrationForm
from . import db, bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods = ['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        client = Client(firstname = form.firstname.data,lastname = form.lastname.data,email = form.email.data,age = form.age.data,password = hashed_password)
        db.session.add(client)
        db.session.commit()
        
        return redirect( url_for('.login') )

    return render_template('signup.html', form = form)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    client = Client.query.filter_by(email = email).first()

    if client is not None and bcrypt.check_password_hash(client.password, password):
        login_user(client)
        return redirect( url_for('main.client_profile') )

    return render_template('login.html')

    #if form.():
       # client = Client.query.filter_by(email = form.email.data).first()
        #if client and (client.password, form.password.data): 
         #   login_user(client)
          #  return redirect( url_for('main.profile') )
        
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect( url_for('auth.login') )

    