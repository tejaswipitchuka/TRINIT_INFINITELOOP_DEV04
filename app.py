import requests
from bs4 import BeautifulSoup
import csv

email=input()
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