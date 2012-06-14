#! /usr/bin/env python
#coding=utf-8

from bottle import route, run, redirect
from mako.template import Template
from main import get_url, get_client

@route('/')
def index():
    mytemplate = Template(filename='template/index.html')
    return mytemplate.render()

@route('/time_line')
def time_line():
    mytemplate = Template(filename='template/imfor.html')
    #i = get_client().get.statuses__user_timeline()
    return mytemplate.render(name="get.imformation")

@route('/add_auth')
def add_auth():
    redirect(get_url())
    
run(host='localhost', port=80)
