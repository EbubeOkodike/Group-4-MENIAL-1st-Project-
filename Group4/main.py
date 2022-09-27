import os
from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user
from .models import Client
from .forms import RegistrationForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/client_profile')
@login_required
def client_profile():
    return render_template('client.html', firstname = current_user.firstname)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/service')
def service():
    return render_template('service.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


@main.route('/blog')
def blog():
    return render_template('blog.html')


