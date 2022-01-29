import requests
from bs4 import BeautifulSoup
import csv
from flask import Flask,render_template,flash,request,redirect,url_for,session,logging
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired,Email,Length
from wtforms import Form,StringField,TextAreaField,PasswordField,BooleanField,SelectField,SubmitField,validators

app=Flask(__name__)

@app.route('/')
def index():
    form=RegisterForm(request.form)
    if request.method=='POST' and form.validate():
        email=form.email.data
    email_list=(list(email.split('.')))
    name=''
    found=0
    for i in range(len(email_list)):
        for j in range(len(email_list[i])):
            if(email_list[i][j].isalpha() and email_list[i][j]!='@'):
                name+=email_list[i][j]
            else:
                found=1
                break
        if(found==1):
            break
    URL = "https://www.google.com/search?q="+name+'+linkedin'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    quotes=[] # a list to store quotes
    table = soup.find('div', attrs = {'class':'kCrYT'})
    temp=table.findAll('div',attrs={'class':'BNeawe UPmit AP7Wnd'})
    #print(temp)
    temp=str(temp)
    start=0
    end=0
    for i in range(len(temp)):
        if(temp[i:i+3]=='com'):
            start=i+6
            break
    for i in range(start,len(temp)):
        if(temp[i]=='<'):
            end=i-1
            break
    ans=temp[start:end+1]
    ans='https://www.linkedin.com/in/'+ans
    print(ans)
    return render_template('index.html')

#Register class
class RegisterForm(Form):
    email=StringField('Email',[validators.Length(min=6,max=50)])

