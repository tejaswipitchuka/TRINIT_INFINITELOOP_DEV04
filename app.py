import requests
from bs4 import BeautifulSoup
import csv
from flask import Flask,render_template,flash,request,redirect,url_for,session,logging
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired,Email,Length
from wtforms import Form,StringField,TextAreaField,PasswordField,BooleanField,SelectField,SubmitField,validators

app=Flask(__name__)


#Register class
class RegisterForm(Form):
    email=StringField('Email',[validators.Length(min=6,max=50)])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)