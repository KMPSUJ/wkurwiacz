#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup as bs
import babel.dates

def next_session_date(my_date=datetime.now()):
    
    #definitions
    url = "https://studiuje.uj.edu.pl/kalendarz-akademicki"
    my_substr="Sesje"
    my_class="highlight-container--no-margin"
    
    #downloading page content
    try:
        page=requests.get(url) 
    except Exception:
        return datetime.max
    
    #parsing page and looking for my_div with class my_class and substr my_substr
    soup=bs(page.text,"html.parser")
    div=soup.find_all('div',class_=my_class)
    my_div=[str(_) for _ in div if str(_).find(my_substr) != -1]
    
    #scrapping dates strings from my_div
    my_div_dates=[] 
    for i in my_div: 
        my_div_dates+=re.findall("od.*roku",i)
    
    #converting dates strings to datetime format
    session_dates=[] 
    for i in my_div_dates:
        year=int(re.search("\d{4}",i).group())
        monthname=re.search("\w{3,}",i).group() 
        day=int(re.search("\d{1,2}",i).group())
        month=list(dict(babel.dates.get_month_names('wide',locale='pl_PL')).values()).index(monthname)+1
        session_dates.append(datetime(year,month,day,8))

    #returning soonest date later than now
    session_dates.sort()    
    for i in session_dates:
        if i > my_date:
            return i
    
    return datetime.max
        
